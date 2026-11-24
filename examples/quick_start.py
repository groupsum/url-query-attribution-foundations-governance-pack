"""Inspect the installed pack identity."""

from ssot_pack_url_query_attribution_foundations import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:url-query-attribution-foundations"
print(metadata["origin"]["id"])
