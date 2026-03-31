# Changelog

All notable changes to **latamdata-py** are documented here.

This project follows [Semantic Versioning](https://semver.org/) and
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/) conventions.

---

## [Unreleased]

### Added
- MkDocs documentation site with Material theme
- `codecov.yml` for coverage reporting
- `tests/conftest.py` with shared pytest fixtures
- Release drafter workflow for automated changelogs
- `SUPPORT.md` with support channels

---

## [0.1.0] — 2025

### Added
- Initial release of latamdata-py
- `list_datasets()` — returns catalog of all available datasets
- `load(dataset_id)` — loads a dataset as a pandas DataFrame
- `info(dataset_id)` — returns metadata dict for a dataset
- Country filtering support via `country=` parameter
- 38+ datasets covering neuroscience, mental health, demography, and education
- GitHub Actions CI pipeline (Python 3.8–3.12 × Linux/Windows/macOS)
- CodeQL security scanning
- Dependabot for automated dependency updates
- `CITATION.cff` and `codemeta.json` for academic citation
- DOI via Zenodo: [10.5281/zenodo.15289327](https://doi.org/10.5281/zenodo.15289327)
- `.devcontainer/devcontainer.json` for GitHub Codespaces
- Spanish README (`README.es.md`)
- `llms.txt` for AI/LLM discoverability

---

[Unreleased]: https://github.com/juanmoisesd/latamdata-py/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/juanmoisesd/latamdata-py/releases/tag/v0.1.0
