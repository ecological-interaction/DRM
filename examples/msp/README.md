# MSP synthetic examples and lightweight checks

All sources, records, decisions, people, ownership and permissions here are
synthetic. The [candidate revision 2](../../DRM_Minimum_Shared_Protocol.md) is
unadopted/unreleased. No real source record or private research excerpt is included.
Phase 4's private documentary pilots are separately closed; these public checks do
not reproduce them. Phase 5 is not authorised. See [provenance](../../PROVENANCE.md).

## Commands from the DRM root

```sh
python3 -B -m unittest discover -s tests -v
python3 -B tools/validate_msp.py templates/development_register.template.json
python3 -B tools/validate_msp.py examples/msp/v2_valid_accepted_unverified.json
python3 -B tools/validate_msp.py examples/msp/v2_valid_file_edition.json
python3 -B tools/validate_msp.py examples/msp/v2_valid_rights_unknown.json
python3 -B tools/validate_msp.py examples/msp/v2_invalid_approved_contested_alignment.json
```

Python 3.8+ standard library; no install/network/PYTHONPATH requirement.
CLI resolves file-edition paths relative to its input JSON directory; the Python
API requires explicit `base_dir` when checking file evidence. Paths cannot escape
that base. Embedded editions recover exact UTF-8 bytes without newline additions.
Hashes/line counts and exact locator quotes are checked; edits need a new retained
edition, not replacement of old citations. Coordinated history rewriting cannot
be detected from a single self-declared snapshot alone.

Exit 0: no detected structural error, possibly explicit limitations. Exit 1:
structural rejection, expected for invalid fixtures. Exit 2: unreadable/malformed
input, duplicate JSON keys or NaN/Infinity. All outcomes retain the assurance
that truth, rights, identity and genuine authority are not verified.

## Format and template

`msp-review-example-1` fixtures and [original oracle](expected_outcomes.json) are
unchanged and checked as legacy only; success does not upgrade to revision 2.
`msp-review-example-2` requires `review_revision: 2` and adds independent proposal,
canonical lifecycle/scientific status, scoped review declarations, evidence
editions, ownership and proportionate rights evidence. Format changes are opt-in,
not a compatible patch or universal scientific-schema mandate.

The [template](../../templates/development_register.template.json) has no actual
proposals. Its synthetic shapes/decision helper are not approvals. Later local
adaptation needs separate authority. For classification extension use origin
scheme owner, local steward, proposal owner and preserved definition/base version.
Methodological changes declare the exception flag; relationships declare typed
endpoints and independent claim/review statuses. Five original proposal types
remain supported; do not copy canonical scientific records into this envelope.

A correction/rework event identifies the same scientific scope/ID before/after;
canonical lifecycle labels remain source-defined. Documentary acceptance does not
change canonical state or scientific evidence. Withdraw only pending proposals;
accepted changes use linked new proposals/supersession, not necessarily a new
scientific identity. A relationship needs independent scoped approval. Identity
unresolved or contested semantics can remain in candidates but block dependent
identity/alignment approval. Rights unknowns restrict use and remain limitations.

## Fixture outcomes

The [format-2 oracle](expected_outcomes_v2.json) is reviewed expected behaviour,
not an automatically generated pass log. Error/limitation code columns are sets.
Twelve unittest methods exercise 48 fixtures plus input, container, template and
file-byte checks. Fifteen structures are valid (five with limitations), and
33 intentionally invalid structures are rejected. These are new synthetic checks,
not historical prototype reproduction, scientific verification or Phase 7.

| Fixture | Exit | Error codes | Limitations |
|---|---:|---|---|
| [valid_register.json](valid_register.json) | 0 | none | none |
| [valid_unresolved_external.json](valid_unresolved_external.json) | 0 | none | UNRESOLVED_EXTERNAL_REFERENCE |
| [valid_declared_exception.json](valid_declared_exception.json) | 0 | none | DECLARED_METHODOLOGICAL_EXCEPTION |
| [valid_lifecycle.json](valid_lifecycle.json) | 0 | none | none |
| [invalid_duplicate_ids.json](invalid_duplicate_ids.json) | 1 | DUPLICATE_ID | none |
| [invalid_missing_provenance.json](invalid_missing_provenance.json) | 1 | PROVENANCE_REQUIRED | none |
| [invalid_transition.json](invalid_transition.json) | 1 | TRANSITION_NOT_PERMITTED | none |
| [invalid_missing_acceptance_decision.json](invalid_missing_acceptance_decision.json) | 1 | DECISION_REQUIRED | none |
| [invalid_malformed_relationship.json](invalid_malformed_relationship.json) | 1 | OBJECT_REQUIRED, TEXT_REQUIRED, UNSUPPORTED_VALUE | none |
| [invalid_internal_reference.json](invalid_internal_reference.json) | 1 | INVALID_INTERNAL_REFERENCE | none |
| [invalid_approved_unresolved.json](invalid_approved_unresolved.json) | 1 | APPROVED_RELATIONSHIP_UNRESOLVED | UNRESOLVED_EXTERNAL_REFERENCE |
| [invalid_version_reuse.json](invalid_version_reuse.json) | 1 | HISTORY_VERSION_REUSED | none |
| [invalid_scheme_ownership.json](invalid_scheme_ownership.json) | 1 | LOCAL_EXTENSION_OWNERSHIP_REQUIRED, SCHEME_REFERENCE_MISMATCH | none |
| [invalid_evidence_status.json](invalid_evidence_status.json) | 1 | UNSUPPORTED_VALUE | none |
| [invalid_declared_authority_role.json](invalid_declared_authority_role.json) | 1 | DECLARED_AUTHORITY_ROLE_MISMATCH | none |
| [invalid_protocol_version.json](invalid_protocol_version.json) | 1 | VERSION_UNSUPPORTED | none |
| [invalid_required_field.json](invalid_required_field.json) | 1 | TEXT_REQUIRED | none |
| [invalid_accepted_self_revision.json](invalid_accepted_self_revision.json) | 1 | TERMINAL_STATE_CHANGED | none |
| [v2_valid_accepted_unverified.json](v2_valid_accepted_unverified.json) | 0 | none | none |
| [v2_valid_correction.json](v2_valid_correction.json) | 0 | none | none |
| [v2_valid_rework.json](v2_valid_rework.json) | 0 | none | none |
| [v2_valid_withdrawal.json](v2_valid_withdrawal.json) | 0 | none | none |
| [v2_valid_supersession.json](v2_valid_supersession.json) | 0 | none | none |
| [v2_valid_file_edition.json](v2_valid_file_edition.json) | 0 | none | none |
| [v2_valid_external_scheme.json](v2_valid_external_scheme.json) | 0 | none | none |
| [v2_valid_multiple_reviews.json](v2_valid_multiple_reviews.json) | 0 | none | none |
| [v2_valid_resolved_contested_candidate.json](v2_valid_resolved_contested_candidate.json) | 0 | none | CONTESTED_MEANING, IDENTITY_UNRESOLVED |
| [v2_valid_rights_unknown.json](v2_valid_rights_unknown.json) | 0 | none | RIGHTS_UNKNOWN, SENSITIVITY_UNKNOWN |
| [v2_valid_rights_restricted.json](v2_valid_rights_restricted.json) | 0 | none | RESTRICTED_USE |
| [v2_invalid_acceptance_implies_verification.json](v2_invalid_acceptance_implies_verification.json) | 1 | SCIENTIFIC_ACCEPTANCE_EVIDENCE_MISSING | none |
| [v2_invalid_correction_identity.json](v2_invalid_correction_identity.json) | 1 | CORRECTION_IDENTITY_CHANGED | none |
| [v2_invalid_withdraw_after_acceptance.json](v2_invalid_withdraw_after_acceptance.json) | 1 | TRANSITION_NOT_PERMITTED | none |
| [v2_invalid_withdraw_missing_decision.json](v2_invalid_withdraw_missing_decision.json) | 1 | ARRAY_REQUIRED, DECISION_REQUIRED, OBJECT_REQUIRED, REQUIRED_SCOPED_REVIEW_MISSING, REVIEW_DECLARATIONS_REQUIRED, TEXT_REQUIRED, UNSUPPORTED_VALUE, WITHDRAWAL_DECISION_REQUIRED | none |
| [v2_invalid_supersession_target.json](v2_invalid_supersession_target.json) | 1 | INVALID_INTERNAL_REFERENCE | none |
| [v2_invalid_embedded_hash.json](v2_invalid_embedded_hash.json) | 1 | EDITION_HASH_MISMATCH | none |
| [v2_invalid_file_hash.json](v2_invalid_file_hash.json) | 1 | EDITION_HASH_MISMATCH | none |
| [v2_invalid_quote.json](v2_invalid_quote.json) | 1 | EVIDENCE_QUOTE_MISMATCH | none |
| [v2_invalid_edition_reference.json](v2_invalid_edition_reference.json) | 1 | EVIDENCE_EDITION_UNDECLARED | none |
| [v2_invalid_extension_steward.json](v2_invalid_extension_steward.json) | 1 | EXTENSION_STEWARDSHIP_MISMATCH | none |
| [v2_invalid_origin_owner_transfer.json](v2_invalid_origin_owner_transfer.json) | 1 | SCHEME_REFERENCE_MISMATCH | none |
| [v2_invalid_missing_domain_review.json](v2_invalid_missing_domain_review.json) | 1 | REQUIRED_SCOPED_REVIEW_MISSING | none |
| [v2_invalid_review_use_scope.json](v2_invalid_review_use_scope.json) | 1 | DECLARED_USE_SCOPE_MISMATCH | none |
| [v2_invalid_approved_identity_unresolved.json](v2_invalid_approved_identity_unresolved.json) | 1 | DEPENDENT_RELATIONSHIP_APPROVAL_BLOCKED | CONTESTED_MEANING, IDENTITY_UNRESOLVED |
| [v2_invalid_approved_contested_alignment.json](v2_invalid_approved_contested_alignment.json) | 1 | DEPENDENT_RELATIONSHIP_APPROVAL_BLOCKED | CONTESTED_MEANING |
| [v2_invalid_rights_review_role.json](v2_invalid_rights_review_role.json) | 1 | REQUIRED_SCOPED_REVIEW_MISSING | none |
| [v2_invalid_duplicate_editions.json](v2_invalid_duplicate_editions.json) | 1 | DUPLICATE_EVIDENCE_EDITION | none |
| [v2_invalid_file_escape.json](v2_invalid_file_escape.json) | 1 | EDITION_PATH_OUTSIDE_BASE, EVIDENCE_LOCATOR_INVALID | none |
| [v2_invalid_structural_review_for_semantics.json](v2_invalid_structural_review_for_semantics.json) | 1 | REQUIRED_SCOPED_REVIEW_MISSING | none |

## Public legacy-golden check

The public legacy oracle includes approved synthetic fixture SHA-256 pins. The
legacy regression verifies these bytes and expected outcomes without opening a
private snapshot. Pins were checked against the prior synthetic edition during
preparation. This does not verify private archive custody or expand legacy checks
to revision-2 conformance. No private history directory is needed.
