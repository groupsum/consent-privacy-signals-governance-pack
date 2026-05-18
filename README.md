# consent-privacy-signals-governance-pack

Installable SSOT governance pack for GPC, GPP, TCF, Consent Mode, DNT, and consent-signal precedence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:consent-privacy-signals`
- Priority: `P0.2`
- PyPI package: `consent-privacy-signals-governance-pack`
- Import package: `ssot_pack_consent_privacy_signals`
- GitHub repository: `groupsum/consent-privacy-signals-governance-pack`
- Reservation owner: `extension-pack:consent-privacy-signals-governance-pack`

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

- `spc:gpc-http-signal-requirements` - GPC HTTP Signal Requirements
- `spc:gpc-javascript-signal-requirements` - GPC JavaScript Signal Requirements
- `spc:dnt-signal-requirements` - DNT Signal Requirements
- `spc:iab-gpp-string-requirements` - IAB GPP String Requirements
- `spc:iab-gpp-section-requirements` - IAB GPP Section Requirements
- `spc:iab-tcf-purpose-requirements` - IAB TCF Purpose Requirements
- `spc:iab-tcf-vendor-requirements` - IAB TCF Vendor Requirements
- `spc:iab-tcf-special-feature-requirements` - IAB TCF Special Feature Requirements
- `spc:google-consent-mode-default-requirements` - Google Consent Mode Default Requirements
- `spc:google-consent-mode-update-requirements` - Google Consent Mode Update Requirements
- `spc:google-consent-mode-storage-requirements` - Google Consent Mode Storage Requirements
- `spc:google-consent-mode-ad-data-requirements` - Google Consent Mode Ad Data Requirements
- `spc:consent-signal-precedence-requirements` - Consent Signal Precedence Requirements
- `spc:consent-signal-evidence-requirements` - Consent Signal Evidence Requirements
- `spc:consent-signal-jurisdiction-requirements` - Consent Signal Jurisdiction Requirements
- `spc:consent-signal-export-requirements` - Consent Signal Export Requirements

## Install With uv

```bash
uv add consent-privacy-signals-governance-pack
uv add ssot-registry consent-privacy-signals-governance-pack
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install consent-privacy-signals-governance-pack
uvx --from ssot-registry ssot pack sync . consent-privacy-signals-governance-pack
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
- PyPI package: https://pypi.org/project/consent-privacy-signals-governance-pack/
- SSOT Registry: https://pypi.org/project/ssot-registry/
