# latamdata-py

**One-line access to 38+ open research datasets from Latin America.**

[![PyPI version](https://badge.fury.io/py/latamdata-py.svg)](https://badge.fury.io/py/latamdata-py)
[![CI](https://github.com/juanmoisesd/latamdata-py/actions/workflows/ci.yml/badge.svg)](https://github.com/juanmoisesd/latamdata-py/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/juanmoisesd/latamdata-py/branch/main/graph/badge.svg)](https://codecov.io/gh/juanmoisesd/latamdata-py)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15289327.svg)](https://doi.org/10.5281/zenodo.15289327)

## Overview

`latamdata-py` is a Python package that provides frictionless access to curated open datasets
covering health, neuroscience, demography, and education across Latin America and Ibero-America.

All datasets are:

- 🔓 **Open access** — freely available under open licenses (CC-BY, CC0)
- 📦 **Versioned** — each release has a persistent DOI
- 🗺 **Georeferenced** — data available at country level
- 📊 **Analysis-ready** — cleaned, documented, and returned as pandas DataFrames

## Quick Install

```bash
pip install latamdata-py
```

## Quick Example

```python
import latamdata as ld

# List all available datasets
datasets = ld.list_datasets()
print(f"Available: {len(datasets)} datasets")

# Load a dataset
df = ld.load("alzheimer-latinamerica-dashboard")
print(df.head())

# Filter by country
df_colombia = ld.load("alzheimer-latinamerica-dashboard", country="CO")
```

## Available Datasets

| Category | Datasets |
|----------|---------|
| 🧠 Neuroscience | Alzheimer's Disease, Brain Connectomics |
| 💊 Mental Health | Specialists per capita, Depression/Anxiety trends |
| 🤖 AI in Research | Generative AI usage/perception |
| 👥 Demography | Population age structure |
| 📚 Education | Educational inequality |

[Browse full catalog →](datasets/catalog.md)

## Citation

If you use latamdata-py in your research, please cite:

```bibtex
@software{delaserna_latamdata_2025,
  author    = {de la Serna, Juan Moisés},
  title     = {latamdata-py: Python package for Latin American open research datasets},
  year      = {2025},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.15289327},
  url       = {https://github.com/juanmoisesd/latamdata-py}
}
```
