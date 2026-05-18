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

- [`adr:uri-query-attribution-boundary`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/adr/ADR-1001-uri-query-attribution-boundary.yaml) - URI Query Attribution Boundary
- [`adr:campaign-parameter-semantics-authority`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/adr/ADR-1002-campaign-parameter-semantics-authority.yaml) - Campaign Parameter Semantics Authority
- [`adr:traffic-source-classification-policy`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/adr/ADR-1003-traffic-source-classification-policy.yaml) - Traffic Source Classification Policy
- [`adr:referrer-observability-policy`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/adr/ADR-1004-referrer-observability-policy.yaml) - Referrer Observability Policy
- [`adr:attribution-state-context-policy`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/adr/ADR-1005-attribution-state-context-policy.yaml) - Attribution State Context Policy
- [`adr:http-metadata-discovery-policy`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/adr/ADR-1006-http-metadata-discovery-policy.yaml) - HTTP Metadata Discovery Policy

## Included SPECs

- [`spc:uri-query-syntax-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2001-uri-query-syntax-requirements.yaml) - URI Query Syntax Requirements
- [`spc:campaign-query-parameter-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2002-campaign-query-parameter-requirements.yaml) - Campaign Query Parameter Requirements
- [`spc:ga4-traffic-source-mapping-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2003-ga4-traffic-source-mapping-requirements.yaml) - GA4 Traffic Source Mapping Requirements
- [`spc:default-channel-classification-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2004-default-channel-classification-requirements.yaml) - Default Channel Classification Requirements
- [`spc:http-request-attribution-context-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2005-http-request-attribution-context-requirements.yaml) - HTTP Request Attribution Context Requirements
- [`spc:referrer-policy-observability-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2006-referrer-policy-observability-requirements.yaml) - Referrer Policy Observability Requirements
- [`spc:fetch-navigation-attribution-context-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2007-fetch-navigation-attribution-context-requirements.yaml) - Fetch And Navigation Attribution Context Requirements
- [`spc:cookie-attribution-state-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2008-cookie-attribution-state-requirements.yaml) - Cookie Attribution State Requirements
- [`spc:web-storage-attribution-state-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2009-web-storage-attribution-state-requirements.yaml) - Web Storage Attribution State Requirements
- [`spc:http-caching-attribution-observability-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2010-http-caching-attribution-observability-requirements.yaml) - HTTP Caching Attribution Observability Requirements
- [`spc:structured-field-attribution-metadata-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2011-structured-field-attribution-metadata-requirements.yaml) - Structured Field Attribution Metadata Requirements
- [`spc:well-known-attribution-metadata-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2012-well-known-attribution-metadata-requirements.yaml) - Well-Known Attribution Metadata Requirements

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
