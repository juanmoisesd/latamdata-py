# API Reference

::: latamdata

## Functions

### list_datasets

```python
latamdata.list_datasets() -> list[dict]
```

Returns a list of all available datasets in the catalog.

**Returns:** List of dicts, each containing:
- `id` (str): Dataset identifier
- `title` (str): Human-readable title
- `doi` (str): Persistent DOI
- `description` (str): Brief description
- `license` (str): License identifier (e.g., "CC-BY-4.0")
- `coverage` (dict): `{"countries": [...], "years": [...]}`

**Example:**
```python
import latamdata as ld

datasets = ld.list_datasets()
for ds in datasets:
    print(ds["id"], "—", ds["title"])
```

---

### load

```python
latamdata.load(
    dataset_id: str,
    country: str | None = None,
    year_start: int | None = None,
    year_end: int | None = None,
) -> pandas.DataFrame
```

Load a dataset as a pandas DataFrame.

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `dataset_id` | `str` | required | Dataset identifier from catalog |
| `country` | `str` | `None` | ISO 3166-1 alpha-2 country code (e.g., `"CO"`) |
| `year_start` | `int` | `None` | Filter rows from this year onwards |
| `year_end` | `int` | `None` | Filter rows up to and including this year |

**Returns:** `pandas.DataFrame`

**Raises:**
- `ValueError`: If `dataset_id` is not found in the catalog
- `ValueError`: If `country` is not a valid ISO 3166-1 alpha-2 code

**Example:**
```python
import latamdata as ld

# Load full dataset
df = ld.load("alzheimer-latinamerica-dashboard")

# Filter by country
df_co = ld.load("alzheimer-latinamerica-dashboard", country="CO")

# Filter by year range
df_recent = ld.load("alzheimer-latinamerica-dashboard", year_start=2010, year_end=2024)
```

---

### info

```python
latamdata.info(dataset_id: str) -> dict
```

Get metadata for a specific dataset.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `dataset_id` | `str` | Dataset identifier from catalog |

**Returns:** Dict with keys: `id`, `title`, `doi`, `url`, `description`, `license`, `coverage`

**Example:**
```python
import latamdata as ld

info = ld.info("alzheimer-latinamerica-dashboard")
print(info["doi"])      # "10.7910/DVN/UVHABW"
print(info["license"])  # "CC-BY-4.0"
print(info["coverage"]) # {"countries": ["AR", ...], "years": [2000, ..., 2050]}
```
