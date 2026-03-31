# Dataset Catalog

Complete list of datasets available in latamdata-py.
All datasets are freely available under open licenses and have persistent DOIs.

## 🧠 Neuroscience & Brain Health

| Dataset ID | Title | DOI | Countries | Years |
|------------|-------|-----|-----------|-------|
| `alzheimer-latinamerica-dashboard` | Alzheimer's Disease in Latin America | [10.7910/DVN/UVHABW](https://doi.org/10.7910/DVN/UVHABW) | 8 | 2000–2050 |
| `human-brain-connectomics-structural-and-functional-connectivity-database` | Human Brain Connectomics | Available | Multiple | Various |

## 💊 Mental Health

| Dataset ID | Title | DOI | Countries | Years |
|------------|-------|-----|-----------|-------|
| `mental-health-specialists-iberoamerica` | Mental Health Specialists per 100k | [10.5281/zenodo.18984813](https://doi.org/10.5281/zenodo.18984813) | 22 | 2000–2026 |
| `mental-health-latin-america-depression-anxiety-suicide-2000-2024` | Depression, Anxiety & Suicide | Available | Latin America | 2000–2024 |
| `global-mental-health-statistics` | Global Mental Health Statistics | Available | Global | Various |
| `psychological-wellbeing-researchers-latam` | Researcher Wellbeing | Available | Latin America | Various |

## 🤖 Technology & Education

| Dataset ID | Title | DOI | Countries | Years |
|------------|-------|-----|-----------|-------|
| `generative-ai-in-academic-research-database-on-usage-perception-and-productivity` | Generative AI in Academic Research | Available | Latin America | 2022–2025 |
| `ai-educational-impact-latin-america-dataset` | AI Educational Impact | Available | Latin America | Various |

## 👥 Demography & Population

| Dataset ID | Title | DOI | Countries | Years |
|------------|-------|-----|-----------|-------|
| `latin-america-population-age-structure-dataset` | Population Age Structure | Available | Latin America | Various |
| `employment-in-latin-america-database-by-country-evolution-2000-2020` | Employment by Country | Available | Latin America | 2000–2020 |

## 🏥 Epidemiology

| Dataset ID | Title | DOI | Countries | Years |
|------------|-------|-----|-----------|-------|
| `epidemiology-alzheimer-latin-america-systematic-review` | Alzheimer Epidemiology Systematic Review | Available | Latin America | Various |
| `long-covid-neuropsychiatric-symptoms-global-2021-2024` | Long COVID Neuropsychiatric Symptoms | Available | Global | 2021–2024 |
| `latin-america-parkinson-epidemiology-database` | Parkinson's Epidemiology | Available | Latin America | Various |
| `adhd-latin-america-synthetic-dataset-prevalence-incidence-gbd-1990-2026` | ADHD in Latin America | Available | Latin America | 1990–2026 |

## 💰 Economics

| Dataset ID | Title | DOI | Countries | Years |
|------------|-------|-----|-----------|-------|
| `colombia-economic-impact-database-indicators-2024-2025` | Colombia Economic Indicators | Available | Colombia | 2024–2025 |
| `costo-economico-salud-mental-global-latam-2020-2024` | Economic Cost of Mental Health | Available | Latin America | 2020–2024 |

---

## How to load a dataset

```python
import latamdata as ld

# Load full dataset
df = ld.load("alzheimer-latinamerica-dashboard")

# Get metadata
info = ld.info("alzheimer-latinamerica-dashboard")
print(info["doi"], info["license"])

# Filter by country (ISO 3166-1 alpha-2)
df_co = ld.load("alzheimer-latinamerica-dashboard", country="CO")
```

!!! tip "Suggest a dataset"
    Missing a dataset you need? [Open a feature request](https://github.com/juanmoisesd/latamdata-py/issues/new?template=feature_request.md)
    and we'll consider adding it to the catalog.
