# Quick Start

Get up and running with latamdata-py in minutes.

## 1. Install

```bash
pip install latamdata-py
```

## 2. List available datasets

```python
import latamdata as ld

datasets = ld.list_datasets()
print(f"Total datasets: {len(datasets)}")

# Preview the first 5
for ds in datasets[:5]:
    print(f"  - {ds['id']}: {ds['title']}")
```

## 3. Get dataset info

```python
info = ld.info("alzheimer-latinamerica-dashboard")
print(info["title"])
print(info["doi"])
print(info["description"])
print(info["coverage"])  # {'countries': ['AR', 'BO', 'BR', ...], 'years': [2000, ..., 2050]}
```

## 4. Load a dataset

```python
df = ld.load("alzheimer-latinamerica-dashboard")
print(df.shape)   # (rows, columns)
print(df.dtypes)
print(df.head())
```

## 5. Filter by country

```python
# ISO 3166-1 alpha-2 country codes
df_co = ld.load("alzheimer-latinamerica-dashboard", country="CO")  # Colombia
df_mx = ld.load("alzheimer-latinamerica-dashboard", country="MX")  # Mexico
df_br = ld.load("alzheimer-latinamerica-dashboard", country="BR")  # Brazil
```

## 6. Filter by year range

```python
df_recent = ld.load("alzheimer-latinamerica-dashboard", year_start=2010, year_end=2024)
```

## 7. Save to file

```python
# Save as CSV
df.to_csv("alzheimer_data.csv", index=False)

# Save as Excel
df.to_excel("alzheimer_data.xlsx", index=False)

# Save as Parquet (efficient for large datasets)
df.to_parquet("alzheimer_data.parquet", index=False)
```

## 8. Quick visualization

```python
import matplotlib.pyplot as plt

df = ld.load("alzheimer-latinamerica-dashboard", country="CO")
df.plot(x="year", y="prevalence_rate", title="Alzheimer Prevalence — Colombia")
plt.tight_layout()
plt.savefig("alzheimer_colombia.png", dpi=150)
plt.show()
```

## Next steps

- [Browse the full dataset catalog](../datasets/catalog.md)
- [API Reference](../api/latamdata.md)
- [Contributing Guide](../contributing.md)
