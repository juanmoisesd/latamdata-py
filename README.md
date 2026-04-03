# latamdata-py: Python Package for Latin American Research Datasets

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19145316-blue?logo=doi)](https://doi.org/10.5281/zenodo.19145316)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--8401--8018-green?logo=orcid)](https://orcid.org/0000-0002-8401-8018)
[![License: CC0](https://img.shields.io/badge/License-CC0%201.0-lightgrey)](http://creativecommons.org/publicdomain/zero/1.0/)
[![GitHub release](https://img.shields.io/github/v/release/juanmoisesd/latamdata-py?label=v1.0.0&logo=github)](https://github.com/juanmoisesd/latamdata-py/releases)
[![CI](https://github.com/juanmoisesd/latamdata-py/actions/workflows/ci.yml/badge.svg)](https://github.com/juanmoisesd/latamdata-py/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/juanmoisesd/latamdata-py/branch/main/graph/badge.svg)](https://codecov.io/gh/juanmoisesd/latamdata-py)
[![Docs](https://img.shields.io/badge/docs-MkDocs-blue?logo=readthedocs)](https://juanmoisesd.github.io/latamdata-py/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/juanmoisesd/latamdata-py/blob/main/examples/basic_usage.py)

> Part of the **[Open Research Collection](https://doi.org/10.5281/zenodo.19145316)** — 1,273+ datasets · Author: [Juan Moisés de la Serna Tuya](https://orcid.org/0000-0002-8401-8018) · [UNIR](https://www.unir.net/)

---

## Overview

**latamdata-py** is a Python package that provides one-line access to 38+ open research datasets from Latin America, covering neuroscience, mental health, epidemiology, and social determinants of health.

All datasets are free, open, and available under CC0 or CC-BY-4.0 licenses.

---

## Installation

```bash
pip install latamdata-py
```

**Requirements:** Python 3.8+ · pandas · requests

---

## Quick Start

```python
import latamdata as ld

# List all available datasets
ld.list_datasets()

# Load a dataset as a pandas DataFrame
df = ld.load("alzheimer-latam")
print(df.head())

# Get metadata for a specific dataset
ld.info("mental-health-specialists")
```

---

## Available Datasets

| Dataset ID | Title | Topic | DOI |
|------------|-------|-------|-----|
| `alzheimer-latam` | Alzheimer's Disease in Latin America (2000–2050) | Neuroscience | [10.7910/DVN/UVHABW](https://doi.org/10.7910/DVN/UVHABW) |
| `mental-health-specialists` | Mental Health Specialists in Ibero-America (2000–2026) | Mental Health | [10.5281/zenodo.18984813](https://doi.org/10.5281/zenodo.18984813) |
| `generative-ai-research` | Generative AI in Academic Research (2022–2025) | AI & Education | — |
| `psychological-wellbeing-latam` | Psychological Wellbeing of Researchers in Latin America | Mental Health | — |
| `global-mental-health` | Global Mental Health Statistics | Epidemiology | — |
| `ai-educational-impact-latam` | AI Educational Impact in Latin America | AI & Education | — |
| `mental-health-lockdown` | Mental Health and Lockdown Dataset | Mental Health | — |
| `adhd-latam` | ADHD in Latin America — GBD 1990–2026 | Neuroscience | — |

Use `ld.list_datasets()` to see the full list of 38+ datasets at runtime.

---

## API Reference

### `latamdata.load(dataset_name, **kwargs)`

Load a dataset as a pandas DataFrame.

```python
df = ld.load("alzheimer-latam")
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `dataset_name` | str | Dataset identifier (see table above) |
| `**kwargs` | | Extra arguments passed to `pandas.read_csv()` |

### `latamdata.list_datasets()`

Returns a DataFrame with all available datasets (name, title, DOI, keywords).

### `latamdata.info(dataset_name)`

Returns a dict with metadata for a single dataset (title, URL, DOI, description, keywords).

---

## Citation

If you use latamdata-py in your research, please cite:

```bibtex
@software{serna_tuya_2026_latamdata,
  author    = {Serna Tuya, Juan Moisés},
  title     = {latamdata-py: One-line access to 38 open research datasets from Latin America},
  year      = {2026},
  version   = {1.0.0},
  doi       = {10.5281/zenodo.19145316},
  url       = {https://github.com/juanmoisesd/latamdata-py}
}
```

---

## License

Code: [MIT](LICENSE) · Data: [CC0 1.0 Universal](http://creativecommons.org/publicdomain/zero/1.0/)

---

<p align="center">
  <a href="https://orcid.org/0000-0002-8401-8018">Juan Moisés de la Serna Tuya</a> ·
  <a href="https://www.unir.net/">UNIR</a> ·
  <a href="https://dataverse.harvard.edu/dataverse/juanmoisesd">Harvard Dataverse</a>
</p>
