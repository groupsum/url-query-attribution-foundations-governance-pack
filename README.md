# url-query-attribution-foundations-governance-pack

<!-- readme-standards:begin branding -->
<p align="center"><a href="https://github.com/groupsum/readme-standards"><img src="https://raw.githubusercontent.com/groupsum/readme-standards/master/docs/assets/readme-standards.svg" alt="Groupsum README Standards" width="300"></a></p>
<p align="center"><strong>url-query-attribution-foundations-governance-pack</strong></p>
<p align="center">Installable SSOT governance pack for URL query parameters, referrer context, UTM conventions, and campaign attribution capture.</p>
<p align="center">
<a href="https://pypi.org/project/url-query-attribution-foundations-governance-pack/"><img alt="pypi: url-query-attribution-foundations-governance-pack" src="https://img.shields.io/pypi/v/url-query-attribution-foundations-governance-pack?labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/pyproject.toml"><img alt="Source version: 0.1.2.dev1" src="https://img.shields.io/static/v1?label=Source%20version&amp;message=0.1.2.dev1&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/pyproject.toml"><img alt="Python: &gt;=3.10,&lt;3.15" src="https://img.shields.io/static/v1?label=Python&amp;message=%3E%3D3.10%2C%3C3.15&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/pyproject.toml"><img alt="Layer: governance" src="https://img.shields.io/static/v1?label=Layer&amp;message=governance&amp;labelColor=1E293B&amp;color=6D28D9"></a>
<a href="https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/README.md#lifecycle-and-migration"><img alt="Lifecycle: active" src="https://img.shields.io/static/v1?label=Lifecycle&amp;message=active&amp;labelColor=1E293B&amp;color=166534"></a>
<a href="https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/static/v1?label=License&amp;message=Apache-2.0&amp;labelColor=1E293B&amp;color=86198F"></a>
<a href="https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/README.md#notices"><img alt="Notice: not required" src="https://img.shields.io/static/v1?label=Notice&amp;message=not%20required&amp;labelColor=1E293B&amp;color=475569"></a>
</p>
<p align="center">
<a href="https://pypi.org/project/url-query-attribution-foundations-governance-pack/"><img alt="Monthly PyPI downloads: url-query-attribution-foundations-governance-pack" src="https://img.shields.io/pypi/dm/url-query-attribution-foundations-governance-pack?labelColor=1E293B&amp;color=0E7490"></a>
<a href="https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/README.md"><img alt="README hits: url-query-attribution-foundations-governance-pack" src="https://hits.sh/github.com/groupsum/url-query-attribution-foundations-governance-pack/README.md.svg?label=README%20hits&amp;labelColor=1E293B&amp;color=0E7490"></a>
</p>
<p align="center">
<a href="https://github.com/groupsum/url-query-attribution-foundations-governance-pack/actions/workflows/readme-standards.yml"><img alt="README standards: CI gate" src="https://img.shields.io/static/v1?label=README%20standards&amp;message=CI%20gate&amp;labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/url-query-attribution-foundations-governance-pack/actions/workflows/readme-standards.yml"><img alt="Tests: package and example checks" src="https://img.shields.io/static/v1?label=Tests&amp;message=package%20and%20example%20checks&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/README.md#certification-status"><img alt="Certification: not certified" src="https://img.shields.io/static/v1?label=Certification&amp;message=not%20certified&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/docs/governance/pack-authoring-guide.md"><img alt="Governance: pack governance" src="https://img.shields.io/static/v1?label=Governance&amp;message=pack%20governance&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/url-query-attribution-foundations-governance-pack/actions/workflows/readme-standards.yml"><img alt="Evidence: README and wheel checks" src="https://img.shields.io/static/v1?label=Evidence&amp;message=README%20and%20wheel%20checks&amp;labelColor=1E293B&amp;color=6D28D9"></a>
</p>
<p align="center"><a href="#overview">Overview</a> · <a href="#installation">Installation</a> · <a href="#quick-start">Quick Start</a> · <a href="#usage">Usage</a> · <a href="#public-api-and-import-surfaces">API</a> · <a href="#contributing">Contributing</a> · <a href="#governance">Governance</a> · <a href="#license">License</a></p>
<!-- readme-standards:end branding -->

---

## Overview

### Summary

Installable SSOT governance pack for URL query parameters, referrer context, UTM conventions, and campaign attribution capture.

### Why This Package

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern url, query, referrer, and campaign parameter foundations, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

### When to Use

Use this pack when a downstream SSOT Registry needs reusable decisions and requirements for URL, Query, Referrer, And Campaign Parameter Foundations.

### Features

**Included ADRs**

- [`adr:uri-query-attribution-boundary`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/adr/ADR-1001-uri-query-attribution-boundary.yaml) — URI Query Attribution Boundary
- [`adr:campaign-parameter-semantics-authority`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/adr/ADR-1002-campaign-parameter-semantics-authority.yaml) — Campaign Parameter Semantics Authority
- [`adr:traffic-source-classification-policy`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/adr/ADR-1003-traffic-source-classification-policy.yaml) — Traffic Source Classification Policy
- [`adr:referrer-observability-policy`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/adr/ADR-1004-referrer-observability-policy.yaml) — Referrer Observability Policy
- [`adr:attribution-state-context-policy`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/adr/ADR-1005-attribution-state-context-policy.yaml) — Attribution State Context Policy
- [`adr:http-metadata-discovery-policy`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/adr/ADR-1006-http-metadata-discovery-policy.yaml) — HTTP Metadata Discovery Policy

**Included SPECs**

- [`spc:uri-query-syntax-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2001-uri-query-syntax-requirements.yaml) — URI Query Syntax Requirements
- [`spc:campaign-query-parameter-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2002-campaign-query-parameter-requirements.yaml) — Campaign Query Parameter Requirements
- [`spc:ga4-traffic-source-mapping-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2003-ga4-traffic-source-mapping-requirements.yaml) — GA4 Traffic Source Mapping Requirements
- [`spc:default-channel-classification-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2004-default-channel-classification-requirements.yaml) — Default Channel Classification Requirements
- [`spc:http-request-attribution-context-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2005-http-request-attribution-context-requirements.yaml) — HTTP Request Attribution Context Requirements
- [`spc:referrer-policy-observability-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2006-referrer-policy-observability-requirements.yaml) — Referrer Policy Observability Requirements
- [`spc:fetch-navigation-attribution-context-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2007-fetch-navigation-attribution-context-requirements.yaml) — Fetch And Navigation Attribution Context Requirements
- [`spc:cookie-attribution-state-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2008-cookie-attribution-state-requirements.yaml) — Cookie Attribution State Requirements
- [`spc:web-storage-attribution-state-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2009-web-storage-attribution-state-requirements.yaml) — Web Storage Attribution State Requirements
- [`spc:http-caching-attribution-observability-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2010-http-caching-attribution-observability-requirements.yaml) — HTTP Caching Attribution Observability Requirements
- [`spc:structured-field-attribution-metadata-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2011-structured-field-attribution-metadata-requirements.yaml) — Structured Field Attribution Metadata Requirements
- [`spc:well-known-attribution-metadata-requirements`](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates/specs/SPEC-2012-well-known-attribution-metadata-requirements.yaml) — Well-Known Attribution Metadata Requirements

### Non-Goals

The pack supplies governance records. A downstream application implements the controls and collects its own conformance evidence.

---

## Getting Started

### Prerequisites

Use Python `>=3.10,<3.15`. Downstream synchronization also requires SSOT Registry and permission to write the target registry.

### Installation

#### uv

<!-- readme-standards:begin installation.uv -->
```bash
uv add url-query-attribution-foundations-governance-pack
```
<!-- readme-standards:end installation.uv -->

#### pip

<!-- readme-standards:begin installation.pip -->
```bash
python -m pip install url-query-attribution-foundations-governance-pack
```
<!-- readme-standards:end installation.pip -->

#### Poetry

<!-- readme-standards:begin installation.poetry -->
```bash
poetry add url-query-attribution-foundations-governance-pack
```
<!-- readme-standards:end installation.poetry -->

### Quick Start

#### Example

<!-- readme-standards:begin example.quick-start -->
Source: [examples/quick_start.py](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/examples/quick_start.py).

```python
"""Inspect the installed pack identity."""

from ssot_pack_url_query_attribution_foundations import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:url-query-attribution-foundations"
print(metadata["origin"]["id"])
```
<!-- readme-standards:end example.quick-start -->

#### Expected Result

The script prints `pack:url-query-attribution-foundations` from the installed pack metadata.

---

## Usage

### Common Workflows

<!-- readme-standards:begin example.usage -->
Source: [examples/usage.py](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/examples/usage.py).

```python
"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_url_query_attribution_foundations import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:uri-query-syntax-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-uri-query-syntax-requirements.yaml"
```
<!-- readme-standards:end example.usage -->

Use the downstream environment that has both SSOT Registry and `url-query-attribution-foundations-governance-pack` installed. Inspect the pack and preflight the target registry before approving synchronization.

```bash
uv run ssot pack inspect ssot_pack_url_query_attribution_foundations
uv run ssot pack preflight . ssot_pack_url_query_attribution_foundations --all
uv run ssot pack sync . ssot_pack_url_query_attribution_foundations --all --trust --yes
uv run ssot validate .
```

### Configuration

Select the installed import package `ssot_pack_url_query_attribution_foundations` in SSOT Registry. Review reservation owner `extension-pack:url-query-attribution-foundations-governance-pack` and the target's trust policy before syncing.

### Error Handling

If preflight reports a schema, trust, or document-number conflict, resolve it in the target registry and repeat preflight before synchronization.

### Best Practices

Pin the pack version in downstream projects. Reference document IDs in local governance and inspect the change set before granting trust.

---

## Package Boundary

### What It Owns

The pack owns the URL, Query, Referrer, And Campaign Parameter Foundations ADRs and SPECs listed under Features.

### Public API and Import Surfaces

Import `load_pack_metadata`, `load_document_manifest`, and `read_packaged_document_text` from `ssot_pack_url_query_attribution_foundations` to inspect packaged records.

### Entry Points

<!-- readme-standards:begin entry-points -->
This package declares no command-line, GUI, or plugin entry points in its manifest.
<!-- readme-standards:end entry-points -->

### Injected Dependencies

The package binds its metadata and document loaders through `ssot-pack-contracts`. The caller supplies the target registry to SSOT Registry when synchronizing.

### Protocol Consumers

SSOT Registry uses the pack metadata, document manifests, and bundled templates during inspect, preflight, and sync.

### Extensions

Define downstream policies as local records and reference the pack's document IDs. Send proposed changes to the canonical pack through repository review.

---

## Operations and Readiness

### Operational Requirements

Local inspection reads installed package resources. Synchronization requires an initialized downstream registry and explicit operator approval.

### Health and Observability

Review the preflight and sync output, then use `ssot validate` to check the resulting registry.

### Security and Resource Limits

Implicit trust is disabled. Review the exact distribution, version, records, and reserved IDs before enabling trust in a target registry.

### Compatibility

- Python `>=3.10,<3.15`
- SSOT Registry schema `>=0.4.0`
- SSOT pack contracts `>=0.2.17,<0.3.0`

---

## Verification

### Tests

Run `python -m unittest discover -s tests -v` with the pack installed. The [README workflow](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/actions/workflows/readme-standards.yml) checks the source README and runs both examples against an installed wheel.

### Certification Status

The pack has no external certification. Downstream adoption requires evidence for the controls an application implements.

### Evidence

See the [README workflow](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/actions/workflows/readme-standards.yml) for package and documentation verification and the [packaged records](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/templates) for document-level sources.

---

## FAQ

### Why

**Why do document IDs matter?** Downstream records use them to trace an adopted decision or requirement to the pack that owns it.

### How

**How do I preview changes?** Use the registry's pack preflight before approving a sync.

### When

**When should I upgrade?** Read the changelog and preflight the new version against the target registry before applying it.

---

## Documentation and Related Packages

### More Documentation

See the [Pack guide](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/docs/pack-guide.md), [changelog](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/CHANGELOG.md), and [pack metadata](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/src/ssot_pack_url_query_attribution_foundations/metadata.json).

### Related Packages

[SSOT Registry](https://pypi.org/project/ssot-registry/) manages downstream registries. [SSOT Pack Contracts](https://pypi.org/project/ssot-pack-contracts/) provides the shared pack interface.

### Project Links

<!-- readme-standards:begin project-links -->
- [Homepage](https://github.com/groupsum/url-query-attribution-foundations-governance-pack)
- [Issues](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/issues)
- [Repository](https://github.com/groupsum/url-query-attribution-foundations-governance-pack)
- [pypi: url-query-attribution-foundations-governance-pack](https://pypi.org/project/url-query-attribution-foundations-governance-pack/)
<!-- readme-standards:end project-links -->

---

## Contributing

### How to Contribute

Open an [issue](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/issues) or pull request describing the affected records, their authority, and the expected downstream effect.

### Development Setup

Install the checkout with `python -m pip install -e .`, then run `python -m unittest discover -s tests -v`. On Python 3.11 or newer, run `uvx --from readme-standards==0.1.3 readme-standards check`.

### Notes for Maintainers

Keep source links, document identifiers, and committed manifest hashes aligned. Run `uvx --from readme-standards==0.1.3 readme-standards render --write` after changing generated README inputs.

---

## Governance

### Ownership and Decision Making

Groupsum maintains `pack:url-query-attribution-foundations`. The pack's reservation owner is `extension-pack:url-query-attribution-foundations-governance-pack`. Downstream registry operators approve synchronization.

### Standards and Policies

**Authority Sources**

- [RFC 3986: Uniform Resource Identifier (URI): Generic Syntax](https://datatracker.ietf.org/doc/html/rfc3986)
- [WHATWG URL Standard](https://url.spec.whatwg.org/)
- [Google Analytics custom campaign URL parameters](https://support.google.com/analytics/answer/10917952)
- [GA4 traffic-source dimensions and manual tagging](https://support.google.com/analytics/answer/11242870)
- [GA4 default channel group](https://support.google.com/analytics/answer/9756891)

### Lifecycle and Migration

Review [release changes](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/CHANGELOG.md) and preflight the chosen version against each downstream registry.

---

## License and Attribution

### License

<!-- readme-standards:begin license -->
Licensed under `Apache-2.0`. See [LICENSE](https://github.com/groupsum/url-query-attribution-foundations-governance-pack/blob/master/LICENSE).
<!-- readme-standards:end license -->

### Notices

<!-- readme-standards:begin notices -->
No separate NOTICE file is declared. Review the license and bundled third-party attributions.
<!-- readme-standards:end notices -->
