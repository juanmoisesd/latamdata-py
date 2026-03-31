"""
Basic usage examples for latamdata-py package.

Installation:
    pip install latamdata-py

Usage:
    python examples/basic_usage.py
"""

import latamdata

# 1. Package information
print("latamdata-py version:", latamdata.__version__)
print("Author:", latamdata.author)

# 2. List available datasets
datasets = latamdata.list_datasets()
print(f"Available datasets ({len(datasets)} total):")
for ds in datasets[:10]:
    print(f"  - {ds}")

# 3. Get dataset metadata
info = latamdata.info("alzheimer_latam")
print("\nDataset: alzheimer_latam")
print(f"  Title  : {info.get('title', 'N/A')}")
print(f"  DOI    : {info.get('doi', 'N/A')}")
print(f"  License: {info.get('license', 'N/A')}")

# 4. Load dataset as pandas DataFrame
df = latamdata.load("alzheimer_latam")
print(f"\nShape: {df.shape}")
print(df.head(3).to_string())

# 5. Filter by country
if "country" in df.columns:
    df_mx = df[df["country"] == "Mexico"]
    print(f"\nMexico rows: {len(df_mx)}")
