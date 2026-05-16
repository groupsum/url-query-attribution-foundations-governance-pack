# ssot-pack-url-query-attribution-foundations

Installable SSOT governance pack for URL query parameters, referrer context, UTM conventions, and campaign attribution capture.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:url-query-attribution-foundations`
- Priority: `P0.1`
- PyPI package: `ssot-pack-url-query-attribution-foundations`
- Import package: `ssot_pack_url_query_attribution_foundations`
- GitHub repository: `groupsum/url-query-attribution-foundations-governance-pack`
- Reservation owner: `extension-pack:ssot-pack-url-query-attribution-foundations`

## Domain Focus

URL, Query, Referrer, And Campaign Parameter Foundations

## Authority Sources

- RFC 3986: Uniform Resource Identifier (URI): Generic Syntax
- WHATWG URL Standard
- Google Analytics custom campaign URL parameters
- GA4 traffic-source dimensions and manual tagging
- GA4 default channel group

## Included ADRs

- `adr:url-query-attribution-boundary` - URL Query Attribution Boundary
- `adr:referrer-and-campaign-capture-policy` - Referrer And Campaign Capture Policy

## Included SPECs

- `spc:uri-query-parameter-contract` - URI Query Parameter Contract
- `spc:referrer-policy-and-http-context-contract` - Referrer Policy And HTTP Context Contract
- `spc:utm-campaign-parameter-contract` - UTM Campaign Parameter Contract
- `spc:traffic-source-classification-contract` - Traffic Source Classification Contract

## Install With uv

```bash
uv add ssot-pack-url-query-attribution-foundations
uv add ssot-registry ssot-pack-url-query-attribution-foundations
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ssot-pack-url-query-attribution-foundations
uvx --from ssot-registry ssot pack sync . ssot-pack-url-query-attribution-foundations
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_pack_url_query_attribution_foundations import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
```

## Resources

- GitHub repository: https://github.com/groupsum/url-query-attribution-foundations-governance-pack
- PyPI package: https://pypi.org/project/ssot-pack-url-query-attribution-foundations/
- SSOT Registry: https://pypi.org/project/ssot-registry/
