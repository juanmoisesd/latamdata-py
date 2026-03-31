# latamdata-py

[![PyPI version](https://badge.fury.io/py/latamdata-py.svg)](https://badge.fury.io/py/latamdata-py)
[![CI](https://github.com/juanmoisesd/latamdata-py/actions/workflows/ci.yml/badge.svg)](https://github.com/juanmoisesd/latamdata-py/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15105434.svg)](https://doi.org/10.5281/zenodo.15105434)

> 🌎 [English README](README.md)

Paquete Python para acceder de forma sencilla a **38+ conjuntos de datos de investigación abiertos** de América Latina con una sola línea de código.

---

## Instalación

```bash
pip install latamdata-py
```

## Uso rápido

```python
import latamdata

# Listar todos los conjuntos de datos disponibles
datasets = latamdata.list_datasets()
print(datasets)

# Ver metadatos de un conjunto de datos
info = latamdata.info("alzheimer_latam")
print(info["title"])   # Alzheimer Latin America Dashboard
print(info["doi"])     # 10.7910/DVN/UVHABW

# Cargar como DataFrame de pandas
df = latamdata.load("alzheimer_latam")
print(df.head())
```

## Conjuntos de datos disponibles

| ID | Tema | DOI | Fuente |
|----|------|-----|--------|
| `alzheimer_latam` | Epidemiología del Alzheimer en Latinoamérica | 10.7910/DVN/UVHABW | Harvard Dataverse |
| `mental_health_specialists` | Especialistas en salud mental por país | 10.5281/zenodo.18984813 | Zenodo |
| `human_brain_connectomics` | Conectómica cerebral estructural y funcional | — | GitHub |
| `generative_ai_academia` | IA generativa en investigación académica | — | GitHub |
| *(+34 más)* | … | … | … |

## Características

- ✅ Acceso con **una línea de código** a más de 38 conjuntos de datos
- ✅ Retorna **DataFrames de pandas** listos para análisis
- ✅ Metadatos completos (DOI, licencia, descripción, número de registros)
- ✅ Compatible con Python 3.9+
- ✅ Sin dependencias pesadas (solo `pandas` y `requests`)

## Instalación para desarrollo

```bash
git clone https://github.com/juanmoisesd/latamdata-py.git
cd latamdata-py
pip install -e ".[dev]"
```

## Ejecutar pruebas

```bash
pytest tests/ -v
```

## Cómo citar

Si usas este paquete en tu investigación, por favor cítalo:

```bibtex
@software{serna_tuya_2025_latamdata,
  author    = {Serna Tuya, Juan Moisés},
  title     = {latamdata-py: Python package for Latin American research datasets},
  year      = {2025},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.15105434},
  url       = {https://github.com/juanmoisesd/latamdata-py}
}
```

## Licencia

MIT © [Juan Moisés de la Serna Tuya](https://github.com/juanmoisesd)

## Contribuir

¡Las contribuciones son bienvenidas! Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para más detalles.
