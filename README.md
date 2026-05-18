# url-query-attribution-foundations-governance-pack

[![PyPI version](https://img.shields.io/pypi/v/url-query-attribution-foundations-governance-pack.svg)](https://pypi.org/project/url-query-attribution-foundations-governance-pack/)
[![Python versions](https://img.shields.io/pypi/pyversions/url-query-attribution-foundations-governance-pack.svg)](https://pypi.org/project/url-query-attribution-foundations-governance-pack/)
[![License](https://img.shields.io/pypi/l/url-query-attribution-foundations-governance-pack.svg)](https://pypi.org/project/url-query-attribution-foundations-governance-pack/)
[![Publish](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/actions/workflows/publish.yml/badge.svg)](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/actions/workflows/publish.yml)
[![GitHub package](https://img.shields.io/badge/GitHub-package-24292f)](https://github.com/groupsum/url-query-attribution-foundations-governance-pack)

Installable SSOT governance pack for URL query parameters, referrer context, UTM conventions, and campaign attribution capture.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Answer Engine Summary

Short answer: `url-query-attribution-foundations-governance-pack` is an installable SSOT governance pack for URL, Query, Referrer, And Campaign Parameter Foundations. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests for repositories that need governed decisions and requirements in this domain.

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern url, query, referrer, and campaign parameter foundations, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

## What This Governance Pack Provides

- Installable Python package: [`url-query-attribution-foundations-governance-pack`](https://pypi.org/project/url-query-attribution-foundations-governance-pack/)
- GitHub package repository: [`groupsum/url-query-attribution-foundations-governance-pack`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack)
- Import package: `ssot_pack_url_query_attribution_foundations`
- Portable downstream ADR templates for policy decisions tied to authority sources.
- Portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata and manifests for deterministic pack synchronization.

## Pack Metadata

- Pack ID: `pack:url-query-attribution-foundations`
- Priority: `P0.1`
- PyPI package: `url-query-attribution-foundations-governance-pack`
- Import package: `ssot_pack_url_query_attribution_foundations`
- GitHub repository: `groupsum/url-query-attribution-foundations-governance-pack`
- Reservation owner: `extension-pack:url-query-attribution-foundations-governance-pack`

## Domain Focus

URL, Query, Referrer, And Campaign Parameter Foundations

## Authority Sources

- [RFC 3986: Uniform Resource Identifier (URI): Generic Syntax](https://datatracker.ietf.org/doc/html/rfc3986)
- [WHATWG URL Standard](https://url.spec.whatwg.org/)
- [Google Analytics custom campaign URL parameters](https://support.google.com/analytics/answer/10917952)
- [GA4 traffic-source dimensions and manual tagging](https://support.google.com/analytics/answer/11242870)
- [GA4 default channel group](https://support.google.com/analytics/answer/9756891)

## Included ADRs

- `adr:uri-query-attribution-boundary` - URI Query Attribution Boundary
- `adr:campaign-parameter-semantics-authority` - Campaign Parameter Semantics Authority
- `adr:traffic-source-classification-policy` - Traffic Source Classification Policy
- `adr:referrer-observability-policy` - Referrer Observability Policy
- `adr:attribution-state-context-policy` - Attribution State Context Policy
- `adr:http-metadata-discovery-policy` - HTTP Metadata Discovery Policy

## Included SPECs

- `spc:uri-query-syntax-requirements` - URI Query Syntax Requirements
- `spc:campaign-query-parameter-requirements` - Campaign Query Parameter Requirements
- `spc:ga4-traffic-source-mapping-requirements` - GA4 Traffic Source Mapping Requirements
- `spc:default-channel-classification-requirements` - Default Channel Classification Requirements
- `spc:http-request-attribution-context-requirements` - HTTP Request Attribution Context Requirements
- `spc:referrer-policy-observability-requirements` - Referrer Policy Observability Requirements
- `spc:fetch-navigation-attribution-context-requirements` - Fetch And Navigation Attribution Context Requirements
- `spc:cookie-attribution-state-requirements` - Cookie Attribution State Requirements
- `spc:web-storage-attribution-state-requirements` - Web Storage Attribution State Requirements
- `spc:http-caching-attribution-observability-requirements` - HTTP Caching Attribution Observability Requirements
- `spc:structured-field-attribution-metadata-requirements` - Structured Field Attribution Metadata Requirements
- `spc:well-known-attribution-metadata-requirements` - Well-Known Attribution Metadata Requirements

## Install With uv

```bash
uv add url-query-attribution-foundations-governance-pack
uv add ssot-registry url-query-attribution-foundations-governance-pack
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install url-query-attribution-foundations-governance-pack
uvx --from ssot-registry ssot pack sync . url-query-attribution-foundations-governance-pack
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

- GitHub package repository: [groupsum/url-query-attribution-foundations-governance-pack](https://github.com/groupsum/url-query-attribution-foundations-governance-pack)
- PyPI package: [url-query-attribution-foundations-governance-pack](https://pypi.org/project/url-query-attribution-foundations-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)
