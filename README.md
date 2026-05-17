# ssot-pack-consent-privacy-signals

Installable SSOT governance pack for GPC, GPP, TCF, Consent Mode, DNT, and consent-signal precedence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:consent-privacy-signals`
- Priority: `P0.2`
- PyPI package: `ssot-pack-consent-privacy-signals`
- Import package: `ssot_pack_consent_privacy_signals`
- GitHub repository: `groupsum/consent-privacy-signals-governance-pack`
- Reservation owner: `extension-pack:ssot-pack-consent-privacy-signals`

## Domain Focus

Consent And Privacy Signal Exchange

## Authority Sources

- Global Privacy Control
- IAB Tech Lab Global Privacy Platform
- IAB Europe Transparency and Consent Framework
- Google Consent Mode
- W3C Tracking Preference Expression / Do Not Track
- IAB Accountability Platform

## Included ADRs

- `adr:consent-signal-source-policy` - Consent Signal Source Policy
- `adr:gpc-signal-policy` - GPC Signal Policy
- `adr:dnt-signal-policy` - DNT Signal Policy
- `adr:iab-gpp-policy` - IAB GPP Policy
- `adr:iab-tcf-policy` - IAB TCF Policy
- `adr:google-consent-mode-policy` - Google Consent Mode Policy
- `adr:consent-default-update-policy` - Consent Default Update Policy
- `adr:consent-precedence-policy` - Consent Precedence Policy
- `adr:consent-signal-evidence-policy` - Consent Signal Evidence Policy
- `adr:consent-signal-jurisdiction-policy` - Consent Signal Jurisdiction Policy

## Included SPECs

- `spc:gpc-signal-contract` - GPC Signal Contract
- `spc:iab-gpp-tcf-contract` - IAB GPP TCF Contract
- `spc:google-consent-mode-contract` - Google Consent Mode Contract
- `spc:consent-precedence-evaluation-contract` - Consent Precedence Evaluation Contract

## Install With uv

```bash
uv add ssot-pack-consent-privacy-signals
uv add ssot-registry ssot-pack-consent-privacy-signals
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ssot-pack-consent-privacy-signals
uvx --from ssot-registry ssot pack sync . ssot-pack-consent-privacy-signals
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_pack_consent_privacy_signals import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
```

## Resources

- GitHub repository: https://github.com/groupsum/consent-privacy-signals-governance-pack
- PyPI package: https://pypi.org/project/ssot-pack-consent-privacy-signals/
- SSOT Registry: https://pypi.org/project/ssot-registry/
