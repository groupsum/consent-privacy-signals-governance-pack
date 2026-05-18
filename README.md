# consent-privacy-signals-governance-pack

[![PyPI version](https://img.shields.io/pypi/v/consent-privacy-signals-governance-pack.svg)](https://pypi.org/project/consent-privacy-signals-governance-pack/)
[![Python versions](https://img.shields.io/pypi/pyversions/consent-privacy-signals-governance-pack.svg)](https://pypi.org/project/consent-privacy-signals-governance-pack/)
[![License](https://img.shields.io/pypi/l/consent-privacy-signals-governance-pack.svg)](https://pypi.org/project/consent-privacy-signals-governance-pack/)
[![Publish](https://github.com/groupsum/consent-privacy-signals-governance-pack/actions/workflows/publish.yml/badge.svg)](https://github.com/groupsum/consent-privacy-signals-governance-pack/actions/workflows/publish.yml)
[![GitHub package](https://img.shields.io/badge/GitHub-package-24292f)](https://github.com/groupsum/consent-privacy-signals-governance-pack)

Installable SSOT governance pack for GPC, GPP, TCF, Consent Mode, DNT, and consent-signal precedence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Answer Engine Summary

Short answer: `consent-privacy-signals-governance-pack` is an installable SSOT governance pack for Consent And Privacy Signal Exchange. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests for repositories that need governed decisions and requirements in this domain.

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern consent and privacy signal exchange, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

## What This Governance Pack Provides

- Installable Python package: [`consent-privacy-signals-governance-pack`](https://pypi.org/project/consent-privacy-signals-governance-pack/)
- GitHub package repository: [`groupsum/consent-privacy-signals-governance-pack`](https://github.com/groupsum/consent-privacy-signals-governance-pack)
- Import package: `ssot_pack_consent_privacy_signals`
- Portable downstream ADR templates for policy decisions tied to authority sources.
- Portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata and manifests for deterministic pack synchronization.

## Pack Metadata

- Pack ID: `pack:consent-privacy-signals`
- PyPI package: `consent-privacy-signals-governance-pack`
- Import package: `ssot_pack_consent_privacy_signals`
- GitHub repository: `groupsum/consent-privacy-signals-governance-pack`
- Reservation owner: `extension-pack:consent-privacy-signals-governance-pack`

## Domain Focus

Consent And Privacy Signal Exchange

## Authority Sources

- [Global Privacy Control](https://globalprivacycontrol.org/)
- [IAB Tech Lab Global Privacy Platform](https://dev.iabtechlab.com/gpp/)
- [IAB Europe Transparency and Consent Framework](https://iabeurope.eu/transparency-consent-framework/)
- [Google Consent Mode](https://developers.google.com/tag-platform/security/guides/consent)
- [W3C Tracking Preference Expression / Do Not Track](https://www.w3.org/TR/tracking-dnt/)
- [IAB Accountability Platform](https://iabtechlab.com/standards/accountability-platform/)

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

- GitHub package repository: [groupsum/consent-privacy-signals-governance-pack](https://github.com/groupsum/consent-privacy-signals-governance-pack)
- PyPI package: [consent-privacy-signals-governance-pack](https://pypi.org/project/consent-privacy-signals-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)
