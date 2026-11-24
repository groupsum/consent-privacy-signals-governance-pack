"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_consent_privacy_signals import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:gpc-http-signal-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-gpc-http-signal-requirements.yaml"
