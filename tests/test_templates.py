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
        self.assertEqual("url-query-attribution-foundations-governance-pack", __ssot_package_name__)
        self.assertEqual("url-query-attribution-foundations-governance-pack", __pypi_package_name__)
        self.assertEqual("1.0.0", metadata["schema_version"])
        self.assertEqual("url-query-attribution-foundations-governance-pack", metadata["ssot_package_name"])
        self.assertEqual("pack:url-query-attribution-foundations", metadata["origin"]["id"])
        self.assertEqual("ssot_pack_url_query_attribution_foundations", metadata["origin"]["import_name"])
        self.assertEqual("governance-pack", metadata["origin"]["kind"])
        self.assertEqual("extension-pack", metadata["trust"]["origin"])
        self.assertEqual("extension-pack:url-query-attribution-foundations-governance-pack", metadata["trust"]["reservation_owner"])
        self.assertFalse(metadata["trust"]["trusted_by_default"])
        self.assertEqual("1.0.0", load_pack_schema_version())

    def test_pack_manifest_contract_is_exposed(self) -> None:
        manifest = load_pack_manifest()
        self.assertEqual("url-query-attribution-foundations-governance-pack", manifest["metadata"]["origin"]["package_name"])
        self.assertEqual(6, len(manifest["documents"]["adr"]))
        self.assertEqual(12, len(manifest["documents"]["spec"]))

    def test_packaged_adr_documents_are_downstream_portable(self) -> None:
        adr_manifest = load_document_manifest("adr")
        self.assertEqual("adr:uri-query-attribution-boundary", adr_manifest[0]["id"])
        for row in adr_manifest:
            text = read_packaged_document_text("adr", row["filename"])
            self.assertNotIn("pack:", text)
            self.assertNotIn("This pack", text)

    def test_packaged_spec_documents_are_downstream_portable(self) -> None:
        spec_manifest = load_document_manifest("spec")
        self.assertEqual("spc:uri-query-syntax-requirements", spec_manifest[0]["id"])
        for row in spec_manifest:
            text = read_packaged_document_text("spec", row["filename"])
            self.assertNotIn("pack:", text)
            self.assertNotIn("This pack", text)


if __name__ == "__main__":
    unittest.main()
