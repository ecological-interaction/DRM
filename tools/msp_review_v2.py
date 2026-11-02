"""Additional bounded review-2 declarations; no scientific schema or authority service."""
import hashlib
from pathlib import Path
import re


def check(root, base_dir):
    errors, limits = [], []
    def error(code, path):
        errors.append({'code': code, 'path': path})
    def limit(code, path):
        limits.append({'code': code, 'path': path})
    def obj(value, path):
        if not isinstance(value, dict):
            error('OBJECT_REQUIRED', path)
            return {}
        return value
    def array(value, path):
        if not isinstance(value, list):
            error('ARRAY_REQUIRED', path)
            return []
        return value
    def text(value, path):
        if not isinstance(value, str) or not value.strip():
            error('TEXT_REQUIRED', path)
            return ''
        return value
    def choice(value, allowed, path):
        if not isinstance(value, str) or value not in allowed:
            error('UNSUPPORTED_VALUE', path)
            return ''
        return value
    if root.get('review_revision') != 2:
        error('REVIEW_REVISION_REQUIRED', '$.review_revision')
    scope = text(root.get('database_scope'), '$.database_scope')
    editions = {}
    for i, value in enumerate(array(root.get('evidence_editions'), '$.evidence_editions')):
        path = f'$.evidence_editions[{i}]'
        edition = obj(value, path)
        ident = text(edition.get('id'), path + '.id')
        if ident in editions:
            error('DUPLICATE_EVIDENCE_EDITION', path)
        kind = choice(edition.get('kind'), {'file', 'embedded'}, path + '.kind')
        text(edition.get('origin'), path + '.origin')
        pin = text(edition.get('sha256'), path + '.sha256')
        if not re.fullmatch('[0-9a-f]{64}', pin):
            error('EDITION_HASH_INVALID', path)
        raw = None
        if kind == 'embedded':
            content = text(edition.get('text'), path + '.text')
            raw = content.encode('utf-8')
        elif kind == 'file':
            name = text(edition.get('path'), path + '.path')
            if base_dir is None:
                error('EVIDENCE_BASE_DIRECTORY_REQUIRED', path)
            else:
                base = Path(base_dir).resolve()
                candidate = (base / name).resolve()
                if not name or Path(name).is_absolute() or base not in candidate.parents:
                    error('EDITION_PATH_OUTSIDE_BASE', path)
                else:
                    try:
                        raw = candidate.read_bytes()
                    except OSError:
                        error('EDITION_FILE_UNAVAILABLE', path)
        if raw is not None:
            if hashlib.sha256(raw).hexdigest() != pin:
                error('EDITION_HASH_MISMATCH', path)
            try:
                lines = raw.decode('utf-8').splitlines()
                if type(edition.get('line_count')) is not int or len(lines) != edition.get('line_count'):
                    error('EDITION_LINE_COUNT_MISMATCH', path)
                editions[ident] = lines
            except UnicodeError:
                error('EDITION_UTF8_REQUIRED', path)
        else:
            editions[ident] = []
    if not editions:
        error('EVIDENCE_EDITIONS_REQUIRED', '$.evidence_editions')

    def reviews(value, path, required, use_scope):
        dec = obj(value, path)
        text(dec.get('reference'), path + '.reference')
        found = set()
        declared = array(dec.get('reviews'), path + '.reviews')
        if not declared:
            error('REVIEW_DECLARATIONS_REQUIRED', path)
        for i, value in enumerate(declared):
            at = f'{path}.reviews[{i}]'
            rev = obj(value, at)
            for field in ['reviewer', 'asserting_authority', 'authority_scope', 'use_scope', 'reference']:
                text(rev.get(field), at + '.' + field)
            role = choice(rev.get('role'), {'domain_authority', 'contract_steward', 'assertion_author',
                         'drm_owner', 'rights_authority', 'proposal_owner'}, at + '.role')
            if rev.get('use_scope') != use_scope:
                error('DECLARED_USE_SCOPE_MISMATCH', at)
            if isinstance(rev.get('authority_scope'), str):
                found.add((role, rev['authority_scope']))
        if not required.issubset(found):
            error('REQUIRED_SCOPED_REVIEW_MISSING', path)

    proposals = [root.get('proposal_template')] if root.get('document_kind') == 'development_register_template' else array(root.get('proposals'), '$.proposals')
    for i, value in enumerate(proposals):
        path = '$.proposal_template' if root.get('document_kind') == 'development_register_template' else f'$.proposals[{i}]'
        p = obj(value, path)
        owner = text(p.get('proposal_owner'), path + '.proposal_owner')
        authority = obj(p.get('asserting_authority'), path + '.asserting_authority')
        text(authority.get('id'), path + '.asserting_authority.id')
        assertion_scope = text(authority.get('scope'), path + '.asserting_authority.scope')
        use = text(p.get('intended_use_scope'), path + '.intended_use_scope')
        canonical = obj(p.get('canonical_record'), path + '.canonical_record')
        for field in ['scope', 'id', 'lifecycle', 'policy_reference']:
            text(canonical.get(field), path + '.canonical_record.' + field)
        known = {(m.get('scope'), m.get('id')) for m in root.get('known_material', []) if isinstance(m, dict)
                 and isinstance(m.get('scope'), str) and isinstance(m.get('id'), str)} if isinstance(root.get('known_material'), list) else set()
        canonical_scope = text(canonical.get('scope'), path + '.canonical_record.scope')
        canonical_id = text(canonical.get('id'), path + '.canonical_record.id')
        identity = (canonical_scope, canonical_id)
        if all(isinstance(x, str) for x in identity) and identity not in known:
            error('CANONICAL_REFERENCE_UNDECLARED', path)
        scientific = obj(p.get('scientific_evidence'), path + '.scientific_evidence')
        status = choice(scientific.get('status'), {'not_assessed', 'not_independently_verified', 'source_reported',
                         'independently_verified'}, path + '.scientific_evidence.status')
        text(scientific.get('basis'), path + '.scientific_evidence.basis')
        if status == 'independently_verified':
            text(scientific.get('review_reference'), path + '.scientific_evidence.review_reference')
        # A declared status never follows from proposal acceptance and is never authenticated.
        for j, value in enumerate(array(p.get('provenance'), path + '.provenance')):
            at = f'{path}.provenance[{j}]'
            prov = obj(value, at)
            ident = text(prov.get('edition_id'), at + '.edition_id')
            loc = obj(prov.get('locator'), at + '.locator')
            a, b = loc.get('line_start'), loc.get('line_end')
            quote = text(loc.get('quote'), at + '.locator.quote')
            if ident not in editions:
                error('EVIDENCE_EDITION_UNDECLARED', at)
            elif type(a) is not int or type(b) is not int or not (1 <= a <= b <= len(editions[ident])):
                error('EVIDENCE_LOCATOR_INVALID', at)
            elif quote != '\n'.join(editions[ident][a-1:b]):
                error('EVIDENCE_QUOTE_MISMATCH', at)
        rights = obj(p.get('rights'), path + '.rights')
        rs = choice(rights.get('status'), {'unknown', 'restricted', 'declared_permitted'}, path + '.rights.status')
        sensitivity = choice(rights.get('sensitivity'), {'unknown', 'public', 'controlled'}, path + '.rights.sensitivity')
        text(rights.get('permitted_use'), path + '.rights.permitted_use')
        text(rights.get('review_reference'), path + '.rights.review_reference')
        if rs == 'unknown':
            limit('RIGHTS_UNKNOWN', path)
        if sensitivity == 'unknown':
            limit('SENSITIVITY_UNKNOWN', path)
        if rs == 'restricted':
            limit('RESTRICTED_USE', path)
        if rs == 'declared_permitted':
            reviews(rights.get('review'), path + '.rights.review', {('rights_authority', canonical_scope)}, use)
        if p.get('proposal_type') == 'classification_extension':
            ext = obj(p.get('classification_extension'), path + '.classification_extension')
            text(ext.get('origin_scheme_owner'), path + '.classification_extension.origin_scheme_owner')
            text(ext.get('local_extension_steward'), path + '.classification_extension.local_extension_steward')
            text(ext.get('proposal_owner'), path + '.classification_extension.proposal_owner')
            text(ext.get('definition_reference'), path + '.classification_extension.definition_reference')
            if ext.get('local_extension_steward') != scope or ext.get('proposal_owner') != owner:
                error('EXTENSION_STEWARDSHIP_MISMATCH', path)
        relationship = p.get('relationship') if isinstance(p.get('relationship'), dict) else {}
        def requirements(purpose):
            if purpose == 'withdrawal':
                return {('proposal_owner', scope)}
            if purpose == 'structural_exchange':
                return {('contract_steward', scope)}
            if purpose == 'research_interpretation':
                return {('assertion_author', assertion_scope)}
            if purpose == 'semantic_alignment':
                needed = set()
                for k in ['source', 'target']:
                    endpoint = relationship.get(k)
                    if isinstance(endpoint, dict) and isinstance(endpoint.get('scope'), str):
                        needed.add(('domain_authority', endpoint['scope']))
                if relationship.get('exchange_use') is True:
                    needed.add(('contract_steward', scope))
                return needed or {('domain_authority', scope)}
            return {('domain_authority', scope)}
        for j, value in enumerate(array(p.get('change_history'), path + '.change_history')):
            at = f'{path}.change_history[{j}]'
            event = obj(value, at)
            if 'action' in event:
                choice(event['action'], {'propose', 'review', 'decision', 'correction', 'rework', 'withdrawal', 'supersession'}, at + '.action')
            if event.get('action') in ('correction', 'rework'):
                before, after = event.get('identity_before'), event.get('identity_after')
                expected = {'scope': canonical_scope, 'id': canonical_id}
                if before != expected or after != expected:
                    error('CORRECTION_IDENTITY_CHANGED', at)
            if event.get('state') in ('reviewed', 'accepted', 'rejected', 'superseded', 'withdrawn'):
                dec = obj(event.get('decision'), at + '.decision')
                purpose = choice(dec.get('purpose'), {'documentary_inclusion', 'scientific_acceptance', 'structural_exchange',
                                 'semantic_alignment', 'research_interpretation', 'withdrawal', 'supersession'}, at + '.decision.purpose')
                if event.get('state') == 'withdrawn' and purpose != 'withdrawal':
                    error('WITHDRAWAL_DECISION_REQUIRED', at)
                needed = requirements(purpose)
                if p.get('methodological_exception') is True:
                    needed |= {('drm_owner', scope)}
                reviews(dec, at + '.decision', needed, use)
                if event.get('state') == 'accepted' and purpose == 'scientific_acceptance' and scientific.get('status') != 'independently_verified':
                    error('SCIENTIFIC_ACCEPTANCE_EVIDENCE_MISSING', at)
        if p.get('proposal_type') == 'relationship':
            claim = choice(relationship.get('claim_kind'), {'identity', 'semantic_alignment', 'functional'}, path + '.relationship.claim_kind')
            ident = choice(relationship.get('identity_status'), {'unresolved', 'supported', 'not_claimed'}, path + '.relationship.identity_status')
            meaning = choice(relationship.get('meaning_status'), {'contested', 'uncontested', 'unassessed'}, path + '.relationship.meaning_status')
            text(relationship.get('claim_evidence_reference'), path + '.relationship.claim_evidence_reference')
            if meaning == 'contested':
                text(relationship.get('disagreement_note'), path + '.relationship.disagreement_note')
                limit('CONTESTED_MEANING', path)
            if ident == 'unresolved':
                limit('IDENTITY_UNRESOLVED', path)
            if relationship.get('review_status') == 'approved':
                if p.get('state') != 'accepted':
                    error('RELATIONSHIP_APPROVAL_REQUIRES_ACCEPTED_PROPOSAL', path)
                if (claim == 'identity' and ident != 'supported') or (claim == 'semantic_alignment' and meaning != 'uncontested'):
                    error('DEPENDENT_RELATIONSHIP_APPROVAL_BLOCKED', path)
                purpose = relationship.get('category')
                purpose = {'structural_mapping': 'structural_exchange', 'source_assertion': 'documentary_inclusion'}.get(purpose, purpose)
                approval = obj(relationship.get('approval'), path + '.relationship.approval')
                if approval.get('purpose') != purpose:
                    error('RELATIONSHIP_APPROVAL_PURPOSE_MISMATCH', path)
                needed = requirements(purpose)
                if claim in {'identity', 'semantic_alignment'}:
                    # A structural category cannot launder an identity/semantic claim.
                    for endpoint_name in ['source', 'target']:
                        endpoint = relationship.get(endpoint_name)
                        if isinstance(endpoint, dict) and isinstance(endpoint.get('scope'), str):
                            needed.add(('domain_authority', endpoint['scope']))
                reviews(approval, path + '.relationship.approval', needed, use)
            if relationship.get('review_status') in ('withdrawn', 'superseded', 'rejected') and relationship.get('review_status') != p.get('state'):
                error('RELATIONSHIP_REVIEW_STATE_MISMATCH', path)
    if root.get('document_kind') == 'development_register_template':
        template = root.get('proposal_template') if isinstance(root.get('proposal_template'), dict) else {}
        reviews(root.get('review_decision_template'), '$.review_decision_template',
                {('domain_authority', scope)}, template.get('intended_use_scope'))
    return {'errors': errors, 'limitations': limits}
