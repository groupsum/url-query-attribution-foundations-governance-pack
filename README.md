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

- `adr:url-query-attribution-pack-boundary` - URL Query Attribution Pack Boundary
- `adr:campaign-parameter-authority-policy` - Campaign Parameter Authority Policy
- `adr:referrer-request-and-session-context-policy` - Referrer Request And Session Context Policy
- `adr:channel-classification-boundary` - Channel Classification Boundary
- `adr:http-state-and-storage-authority-policy` - HTTP State And Storage Authority Policy
- `adr:metadata-discovery-and-structured-field-policy` - Metadata Discovery And Structured Field Policy

## Included SPECs

- `spc:rfc3986-uri-query-syntax-contract` - RFC 3986 URI Query Syntax Contract
- `spc:whatwg-url-parsing-contract` - WHATWG URL Parsing Contract
- `spc:utm-campaign-parameter-contract` - UTM Campaign Parameter Contract
- `spc:ga4-traffic-source-mapping-contract` - GA4 Traffic Source Mapping Contract
- `spc:ga4-default-channel-classification-contract` - GA4 Default Channel Classification Contract
- `spc:http-request-context-contract` - HTTP Request Context Contract
- `spc:http-state-attribution-context-contract` - HTTP State Attribution Context Contract
- `spc:http-state-modern-cookie-contract` - Modern Cookie Attribution Context Contract
- `spc:referrer-policy-attribution-contract` - Referrer Policy Attribution Contract
- `spc:http-caching-attribution-observability-contract` - HTTP Caching Attribution Observability Contract
- `spc:http-structured-fields-support-contract` - HTTP Structured Fields Support Contract
- `spc:well-known-uri-discovery-contract` - Well-Known URI Discovery Contract
- `spc:fetch-request-attribution-context-contract` - Fetch Request Attribution Context Contract
- `spc:html-navigation-attribution-context-contract` - HTML Navigation Attribution Context Contract
- `spc:web-storage-attribution-context-contract` - Web Storage Attribution Context Contract

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
