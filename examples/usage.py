"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_url_query_attribution_foundations import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:uri-query-syntax-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-uri-query-syntax-requirements.yaml"
