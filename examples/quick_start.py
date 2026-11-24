"""Inspect the installed pack identity."""

from ssot_pack_consent_privacy_signals import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:consent-privacy-signals"
print(metadata["origin"]["id"])
