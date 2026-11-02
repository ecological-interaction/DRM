# DRM — Database Reference Methodology

DRM is a methodological and technical framework for designing, developing,
evaluating, governing and connecting heterogeneous research databases.
It standardises accountable methods and exchange contracts while preserving
each database's scientific meanings, evidence, classifications and authority.
It does not prescribe a universal scientific ontology or storage engine.

**Development status — 1 November 2026:** Phases 1–3 have completed their
documented development work. The AMRKB and OSDS bounded documentary preservation
pilots were separately accepted and Phase 4 is closed. **Phase 5 is not authorised;
Phases 5–8 remain future work.** DRM-MSP 0.1.0 review revision 2 is a candidate,
not an adopted/released protocol or a DRM v1.0 conformance certificate.

This is a separately curated public-facing preparation edition. No Git repository
has been initialised here, and publication or a software licence has not been
approved by preparing it. See [provenance and limitations](PROVENANCE.md).

## Read the framework

- [Architecture and Remit](DRM_Architecture_and_Remit.md): responsibilities and boundaries.
- [Methodological Architecture](DRM_Methodological_Architecture.md): twelve principles,
  six iterative A–F stages, profile accountability and approval limits.
- [Eight-phase roadmap](DRM_v1_Roadmap.md): development sequence and future gates.
- [Decision summary](DECISIONS.md): approved principles, bounded acceptance and open questions.
- [Minimum Shared Protocol candidate](DRM_Minimum_Shared_Protocol.md): seven subjects
  and separate proposal/canonical/scientific status.
- [Examples and commands](examples/msp/README.md): synthetic fixtures and bounded checks.
- [Development status](DEVELOPMENT_STATUS.md): available capabilities and remaining gates.
- [Changelog](CHANGELOG.md) and [citation metadata](CITATION.cff).

## Try the synthetic checks

Python 3.8 or later, standard library only. Run from this directory:

```sh
python3 -B -m unittest discover -s tests -v
python3 -B tools/validate_msp.py templates/development_register.template.json
python3 -B tools/validate_msp.py examples/msp/v2_valid_accepted_unverified.json
```

The template is synthetic and unpopulated. Tests cover 48 synthetic fixtures plus
focused robustness checks. An invalid fixture being rejected is its expected
outcome. Exit 0 means no detected structural error, possibly explicit limitations;
it does not prove scientific truth, rights, genuine reviewer authority or identity.
These checks do not reproduce private pilots or the reported historical prototype.

## Methodology and responsibility

A–F concern each database's design: domain requirements, knowledge modelling,
engineering, analytical methods, lifecycle, interoperability/governance. They are
iterative and distinct from the eight phases for developing DRM itself.

Domain databases own their records and interpretations. Federation infrastructure
implements shared contracts. IRKB conducts independent interdisciplinary research
and synthesis; applications need not pass through IRKB to access source databases.
Methodological accountability, technical conformance and scientific validity are
separate judgements. Optional classifications, specialist models and storage
technologies remain domain choices.

## Available and future capabilities

Available here: curated methodological documentation, a candidate minimum profile,
an empty proposal-register template, synthetic examples and lightweight checks.
Not established here: operational federation registries, production ingestion,
external connectors, real-data adapters, full conformance validation or DRM v1.0.
Candidate standards and Zotero/Zenodo integration are planned work, not implemented
or verified integrations. No licence or reuse permission is implied by visibility.
