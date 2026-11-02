#!/usr/bin/env python3
"""Structural checks for the DRM-MSP review examples/template, not scientific approval."""
import argparse
import datetime
import json
import importlib.util
from pathlib import Path

PROTOCOL = "DRM-MSP 0.1.0"
FORMAT = "msp-review-example-1"
FORMAT2 = "msp-review-example-2"
TYPES = {"proposed_record", "classification_extension", "methodological_change", "relationship", "schema_change"}
STATES = {"proposed", "reviewed", "accepted", "rejected", "superseded"}
NEXT = {"proposed": {"reviewed", "rejected"}, "reviewed": {"proposed", "accepted", "rejected"},
        "accepted": {"superseded"}, "rejected": set(), "superseded": set()}
EVIDENCE = {"source_reported", "proposal", "historical_documentation", "synthetic_example", "independently_verified"}
CATEGORIES = {"structural_mapping", "semantic_alignment", "source_assertion", "research_interpretation"}
ROLES = {"domain_authority", "contract_steward", "assertion_author", "drm_owner", "rights_authority"}


def validate(document, base_dir=None):
    errors, limitations = [], []

    def fail(code, path):
        errors.append({"code": code, "path": path})

    def obj(value, path):
        if not isinstance(value, dict):
            fail("OBJECT_REQUIRED", path)
            return {}
        return value

    def arr(value, path):
        if not isinstance(value, list):
            fail("ARRAY_REQUIRED", path)
            return []
        return value

    def text(value, path):
        if not isinstance(value, str) or not value.strip():
            fail("TEXT_REQUIRED", path)
            return ""
        return value

    def choice(value, allowed, path):
        if not isinstance(value, str) or value not in allowed:
            fail("UNSUPPORTED_VALUE", path)
            return ""
        return value

    root = obj(document, "$")
    kind = choice(root.get("document_kind"), {"synthetic_examples", "development_register_template"}, "$.document_kind")
    revised = root.get("format_version") == FORMAT2
    states = STATES | {"withdrawn"} if revised else STATES
    transitions = {k: set(v) for k, v in NEXT.items()}
    if revised:
        transitions["proposed"].add("withdrawn")
        transitions["reviewed"].add("withdrawn")
        transitions["withdrawn"] = set()
    if root.get("protocol") != PROTOCOL or root.get("format_version") not in (FORMAT, FORMAT2):
        fail("VERSION_UNSUPPORTED", "$")
    scope = text(root.get("database_scope"), "$.database_scope")
    if kind == "synthetic_examples" and root.get("synthetic") is not True:
        fail("SYNTHETIC_LABEL_REQUIRED", "$.synthetic")
    if kind == "development_register_template":
        text(root.get("instructions"), "$.instructions")
    material, schemes, types = set(), set(), set()
    identifiers = set()
    for n, value in enumerate(arr(root.get("known_material"), "$.known_material")):
        path = f"$.known_material[{n}]"
        item = obj(value, path)
        key = (text(item.get("scope"), path + ".scope"), text(item.get("id"), path + ".id"))
        if key in identifiers:
            fail("DUPLICATE_ID", path)
        identifiers.add(key)
        material.add(key)
    for n, value in enumerate(arr(root.get("classification_schemes"), "$.classification_schemes")):
        path = f"$.classification_schemes[{n}]"
        item = obj(value, path)
        key = tuple(text(item.get(k), path + "." + k) for k in ("owner", "id", "version"))
        if key in schemes:
            fail("DUPLICATE_SCHEME", path)
        schemes.add(key)
    for n, value in enumerate(arr(root.get("relationship_types"), "$.relationship_types")):
        path = f"$.relationship_types[{n}]"
        name = text(value, path)
        if name in types:
            fail("DUPLICATE_RELATIONSHIP_TYPE", path)
        types.add(name)

    def reference(value, path):
        ref = obj(value, path)
        key = (text(ref.get("scope"), path + ".scope"), text(ref.get("id"), path + ".id"))
        rk = choice(ref.get("kind"), {"internal", "external"}, path + ".kind")
        resolution = choice(ref.get("resolution"), {"resolved", "unresolved"}, path + ".resolution")
        if rk == "internal":
            if key[0] != scope or key not in material or resolution != "resolved":
                fail("INVALID_INTERNAL_REFERENCE", path)
        elif rk == "external":
            if key[0] == scope:
                fail("EXTERNAL_SCOPE_REQUIRED", path)
            if resolution == "unresolved":
                text(ref.get("reason"), path + ".reason")
                limitations.append({"code": "UNRESOLVED_EXTERNAL_REFERENCE", "path": path})
            elif resolution == "resolved":
                text(ref.get("evidence"), path + ".evidence")
        return resolution

    def decision(value, path, allowed_roles):
        if revised:
            return  # Review-2 declarations are checked independently below.
        dec = obj(value, path)
        for field in ("reference", "reviewer", "authority_scope"):
            text(dec.get(field), path + "." + field)
        role = choice(dec.get("authority_role"), ROLES, path + ".authority_role")
        if role and role not in allowed_roles:
            fail("DECLARED_AUTHORITY_ROLE_MISMATCH", path)
        if dec.get("authority_scope") != scope:
            fail("DECLARED_AUTHORITY_SCOPE_MISMATCH", path)

    proposals = arr(root.get("proposals"), "$.proposals")
    if kind == "development_register_template":
        if proposals:
            fail("TEMPLATE_MUST_NOT_CONTAIN_OPERATIONAL_PROPOSALS", "$.proposals")
        proposals = [root.get("proposal_template")]
        decision(root.get("review_decision_template"), "$.review_decision_template", ROLES)
    for n, value in enumerate(proposals):
        path = "$.proposal_template" if kind == "development_register_template" else f"$.proposals[{n}]"
        p = obj(value, path)
        pid = text(p.get("id"), path + ".id")
        db = text(p.get("database"), path + ".database")
        if db != scope:
            fail("PROPOSAL_SCOPE_MISMATCH", path)
        if (db, pid) in identifiers:
            fail("DUPLICATE_ID", path)
        identifiers.add((db, pid))
        pt = choice(p.get("proposal_type"), TYPES, path + ".proposal_type")
        state = choice(p.get("state"), states, path + ".state")
        text(p.get("rationale"), path + ".rationale")
        affected = arr(p.get("affected_material"), path + ".affected_material")
        if pt != "proposed_record" and not affected:
            fail("AFFECTED_MATERIAL_REQUIRED", path)
        for j, ref in enumerate(affected):
            reference(ref, f"{path}.affected_material[{j}]")
        prov = arr(p.get("provenance"), path + ".provenance")
        if not prov:
            fail("PROVENANCE_REQUIRED", path)
        for j, value in enumerate(prov):
            at = f"{path}.provenance[{j}]"
            source = obj(value, at)
            text(source.get("source"), at + ".source")
            text(source.get("contributor_or_process"), at + ".contributor_or_process")
            choice(source.get("evidence_status"), EVIDENCE, at + ".evidence_status")
        versions = obj(p.get("versions"), path + ".versions")
        text(versions.get("record"), path + ".versions.record")
        text(versions.get("schema"), path + ".versions.schema")
        if versions.get("protocol") != PROTOCOL:
            fail("VERSION_UNSUPPORTED", path + ".versions.protocol")
        if "classification" not in versions or (versions["classification"] is not None and
                (not isinstance(versions["classification"], str) or not versions["classification"].strip())):
            fail("CLASSIFICATION_VERSION_REQUIRED_OR_NULL", path + ".versions.classification")
        ext = p.get("classification_extension")
        if pt == "classification_extension":
            ext = obj(ext, path + ".classification_extension")
            key = tuple(text(ext.get(k), path + ".classification_extension." + k) for k in (("origin_scheme_owner", "scheme", "version") if revised else ("owner", "scheme", "version")))
            if key not in schemes or versions.get("classification") != key[2]:
                fail("SCHEME_REFERENCE_MISMATCH", path)
            if ext.get("status") != "provisional_local" or (not revised and key[0] != scope):
                fail("LOCAL_EXTENSION_OWNERSHIP_REQUIRED", path)
        elif ext is not None:
            fail("UNEXPECTED_CLASSIFICATION_EXTENSION", path)
        rel = p.get("relationship")
        category = ""
        if pt == "relationship":
            rel = obj(rel, path + ".relationship")
            rt = text(rel.get("type"), path + ".relationship.type")
            if rt not in types:
                fail("RELATIONSHIP_TYPE_UNDECLARED", path)
            category = choice(rel.get("category"), CATEGORIES, path + ".relationship.category")
            resolutions = [reference(rel.get(k), path + ".relationship." + k) for k in ("source", "target")]
            rs = choice(rel.get("review_status"), {"candidate", "reviewed", "approved", "rejected", "superseded", "withdrawn"} if revised else {"candidate", "reviewed", "approved", "rejected", "superseded"}, path + ".relationship.review_status")
            expected = {"proposed": "candidate", "reviewed": "reviewed", "accepted": "approved", "rejected": "rejected", "superseded": "superseded"}
            if not revised and state and rs != expected[state]:
                fail("RELATIONSHIP_REVIEW_STATE_MISMATCH", path)
            if rs == "approved" and "unresolved" in resolutions:
                fail("APPROVED_RELATIONSHIP_UNRESOLVED", path)
        elif rel is not None:
            fail("UNEXPECTED_RELATIONSHIP", path)
        roles = {"domain_authority"}
        if pt == "methodological_change":
            exception = p.get("methodological_exception")
            if not isinstance(exception, bool):
                fail("EXCEPTION_FLAG_REQUIRED", path)
            if exception is True:
                roles = {"drm_owner"}
                limitations.append({"code": "DECLARED_METHODOLOGICAL_EXCEPTION", "path": path})
        if category == "structural_mapping":
            roles = {"contract_steward"}
        elif category == "research_interpretation":
            roles = {"assertion_author"}
        history = arr(p.get("change_history"), path + ".change_history")
        if not history:
            fail("HISTORY_REQUIRED", path)
        prev, seen_versions, last_date = None, set(), None
        for j, value in enumerate(history):
            at = f"{path}.change_history[{j}]"
            event = obj(value, at)
            es = choice(event.get("state"), states, at + ".state")
            rv = text(event.get("record_version"), at + ".record_version")
            text(event.get("summary"), at + ".summary")
            text(event.get("actor"), at + ".actor")
            try:
                date = datetime.date.fromisoformat(event.get("date", ""))
                if last_date and date < last_date:
                    fail("HISTORY_DATE_ORDER", at)
                last_date = date
            except (TypeError, ValueError):
                fail("DATE_INVALID", at)
            if rv in seen_versions:
                fail("HISTORY_VERSION_REUSED", at)
            seen_versions.add(rv)
            if j == 0 and es != "proposed":
                fail("INITIAL_STATE_MUST_BE_PROPOSED", at)
            if j and es != prev and es not in transitions.get(prev, set()):
                fail("TRANSITION_NOT_PERMITTED", at)
            if j and es == prev and es in {"accepted", "rejected", "superseded", "withdrawn"}:
                fail("TERMINAL_STATE_CHANGED", at)
            if es in {"reviewed", "accepted", "rejected", "superseded", "withdrawn"}:
                if not isinstance(event.get("decision"), dict):
                    fail("DECISION_REQUIRED", at)
                else:
                    decision(event["decision"], at + ".decision", roles)
            if es == "superseded":
                reference(event.get("superseded_by"), at + ".superseded_by")
            prev = es
        if history:
            last = obj(history[-1], path + ".change_history[-1]")
            if last.get("state") != state or last.get("record_version") != versions.get("record"):
                fail("CURRENT_HISTORY_MISMATCH", path)
    if revised:
        helper_path = Path(__file__).with_name("msp_review_v2.py")
        spec = importlib.util.spec_from_file_location("msp_review_v2", helper_path)
        helper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(helper)
        extra = helper.check(root, base_dir)
        errors.extend(extra["errors"])
        limitations.extend(extra["limitations"])
    return {"valid_structure": not errors,
            "outcome": "invalid" if errors else ("valid_structure_with_limitations" if limitations else "valid_structure"),
            "errors": errors, "limitations": limitations,
            "checked_format": root.get("format_version"),
            "check_scope": "Review-2 example declarations" if revised else "Legacy format-1 checks only; no review-2 conformance claim",
            "assurance": "Structure and declared evidence only; scientific truth, rights, identity equivalence and actual reviewer authority are not verified."}


def load_document(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON key: " + key)
            result[key] = value
        return result
    def no_constant(value):
        raise ValueError("non-JSON constant: " + value)
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=unique, parse_constant=no_constant)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="MSP synthetic example or template JSON")
    args = parser.parse_args()
    try:
        result = validate(load_document(args.path), base_dir=Path(args.path).resolve().parent)
    except (OSError, UnicodeError, ValueError, RecursionError) as exc:
        print(json.dumps({"outcome": "input_error", "error": str(exc)}))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["valid_structure"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
