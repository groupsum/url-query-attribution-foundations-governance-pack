from __future__ import annotations

import unittest

from ssot_pack_url_query_attribution_foundations import (
    __pypi_package_name__,
    __ssot_package_name__,
    load_document_manifest,
    load_pack_manifest,
    load_pack_metadata,
    load_pack_schema_version,
    read_packaged_document_text,
)


class GovernancePackManifestTests(unittest.TestCase):
    def test_pack_metadata_contract_is_exposed(self) -> None:
        metadata = load_pack_metadata()
        self.assertEqual("ssot-pack-url-query-attribution-foundations", __ssot_package_name__)
        self.assertEqual("ssot-pack-url-query-attribution-foundations", __pypi_package_name__)
        self.assertEqual("1.0.0", metadata["schema_version"])
        self.assertEqual("ssot-pack-url-query-attribution-foundations", metadata["ssot_package_name"])
        self.assertEqual("pack:url-query-attribution-foundations", metadata["origin"]["id"])
        self.assertEqual("ssot_pack_url_query_attribution_foundations", metadata["origin"]["import_name"])
        self.assertEqual("governance-pack", metadata["origin"]["kind"])
        self.assertEqual("extension-pack", metadata["trust"]["origin"])
        self.assertEqual("extension-pack:ssot-pack-url-query-attribution-foundations", metadata["trust"]["reservation_owner"])
        self.assertFalse(metadata["trust"]["trusted_by_default"])
        self.assertEqual("1.0.0", load_pack_schema_version())

    def test_pack_manifest_contract_is_exposed(self) -> None:
        manifest = load_pack_manifest()
        self.assertEqual("ssot-pack-url-query-attribution-foundations", manifest["metadata"]["origin"]["package_name"])
        self.assertEqual(6, len(manifest["documents"]["adr"]))
        self.assertEqual(4, len(manifest["documents"]["spec"]))

    def test_packaged_documents_are_readable(self) -> None:
        adr_manifest = load_document_manifest("adr")
        spec_manifest = load_document_manifest("spec")
        self.assertEqual("adr:url-query-attribution-pack-boundary", adr_manifest[0]["id"])
        self.assertEqual("spc:uri-query-parameter-contract", spec_manifest[0]["id"])
        self.assertIn("pack:url-query-attribution-foundations", read_packaged_document_text("adr", adr_manifest[0]["filename"]))
        self.assertIn("URL, Query, Referrer, And Campaign Parameter Foundations", read_packaged_document_text("spec", spec_manifest[0]["filename"]))


if __name__ == "__main__":
    unittest.main()
