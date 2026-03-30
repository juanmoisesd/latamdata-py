"""
Main dataset loading module for latamdata-py.

Provides one-line access to open research datasets from Latin America.
Datasets are fetched from their public GitHub repositories.
"""

import pandas as pd
import requests
import json
from pathlib import Path
from typing import Optional, Union

# Dataset registry
_REGISTRY = {
    "alzheimer-latam": {
        "title": "Alzheimer's Disease in Latin America (2000-2050)",
        "url": "https://raw.githubusercontent.com/juanmoisesd/alzheimer-latinamerica-dashboard/main/data/alzheimer_latam.csv",
        "doi": "10.7910/DVN/UVHABW",
        "description": "Alzheimer prevalence, projections, policy index and caregiver burden for 8 Latin American countries.",
        "keywords": ["alzheimer", "dementia", "latin america", "epidemiology"],
        "language": "en"
    },
    "mental-health-specialists": {
        "title": "Mental Health Specialists in Ibero-America (2000-2026)",
        "url": "https://raw.githubusercontent.com/juanmoisesd/mental-health-specialists-iberoamerica/main/data/specialists.csv",
        "doi": "10.5281/zenodo.18984813",
        "description": "Mental health and neurology specialists per 100k inhabitants in Ibero-America.",
        "keywords": ["mental health", "neurology", "ibero-america", "health workforce"],
        "language": "en"
    },
    "generative-ai-research": {
        "title": "Generative AI in Academic Research (2022-2025)",
        "url": "https://raw.githubusercontent.com/juanmoisesd/generative-ai-in-academic-research-database-on-usage-perception-and-productivity/main/data/genai_research.csv",
        "doi": None,
        "description": "Database on generative AI usage, perception and productivity in Latin American universities.",
        "keywords": ["generative AI", "academic research", "higher education", "latin america"],
        "language": "en"
    },
    "psychological-wellbeing-latam": {
        "title": "Psychological Wellbeing of Researchers in Latin America",
        "url": "https://raw.githubusercontent.com/juanmoisesd/psychological-wellbeing-researchers-latam/main/data/wellbeing.csv",
        "doi": None,
        "description": "Survey data on psychological wellbeing, burnout and resilience among researchers in Latin America.",
        "keywords": ["psychology", "wellbeing", "researchers", "latin america"],
        "language": "en"
    },
    "global-mental-health": {
        "title": "Global Mental Health Statistics",
        "url": "https://raw.githubusercontent.com/juanmoisesd/global-mental-health-statistics/main/data/global_mental_health.csv",
        "doi": None,
        "description": "Global statistics on mental health disorders, treatment gap and policy indicators.",
        "keywords": ["mental health", "global", "statistics", "epidemiology"],
        "language": "en"
    },
    "ai-educational-impact-latam": {
        "title": "AI Educational Impact in Latin America",
        "url": "https://raw.githubusercontent.com/juanmoisesd/ai-educational-impact-latin-america-dataset/main/data/ai_education.csv",
        "doi": None,
        "description": "Dataset on the impact of artificial intelligence on educational outcomes in Latin America.",
        "keywords": ["AI", "education", "latin america", "impact"],
        "language": "en"
    },
    "mental-health-lockdown": {
        "title": "Mental Health and Lockdown Dataset",
        "url": "https://raw.githubusercontent.com/juanmoisesd/mental-health-and-lockdown-dataset/main/data/lockdown_mental_health.csv",
        "doi": None,
        "description": "Dataset on mental health outcomes during COVID-19 lockdowns.",
        "keywords": ["mental health", "lockdown", "COVID-19", "anxiety", "depression"],
        "language": "en"
    },
    "adhd-latam": {
        "title": "ADHD in Latin America (GBD 1990-2026)",
        "url": "https://raw.githubusercontent.com/juanmoisesd/adhd-latin-america-synthetic-dataset-prevalence-incidence-gbd-1990-2026/main/data/adhd_latam.csv",
        "doi": None,
        "description": "Synthetic dataset on ADHD prevalence and incidence in Latin America based on GBD data (1990-2026).",
        "keywords": ["ADHD", "latin america", "GBD", "prevalence", "incidence"],
        "language": "en"
    }
}


def list_datasets() -> pd.DataFrame:
    """
    List all available datasets in the latamdata-py registry.
    
    Returns
    -------
    pd.DataFrame
        DataFrame with columns: name, title, doi, keywords, language.
    
    Examples
    --------
    >>> import latamdata as ld
    >>> ld.list_datasets()
    """
    rows = []
    for name, meta in _REGISTRY.items():
        rows.append({
            "name": name,
            "title": meta["title"],
            "doi": meta.get("doi", ""),
            "keywords": ", ".join(meta.get("keywords", [])),
            "language": meta.get("language", "en")
        })
    return pd.DataFrame(rows)


def info(dataset_name: str) -> dict:
    """
    Get metadata about a specific dataset.
    
    Parameters
    ----------
    dataset_name : str
        Name of the dataset (use list_datasets() to see available names).
    
    Returns
    -------
    dict
        Dictionary with dataset metadata.
    
    Examples
    --------
    >>> import latamdata as ld
    >>> ld.info("alzheimer-latam")
    """
    if dataset_name not in _REGISTRY:
        available = list(_REGISTRY.keys())
        raise ValueError(f"Dataset '{dataset_name}' not found. Available datasets: {available}")
    return _REGISTRY[dataset_name].copy()


def load(
    dataset_name: str,
    use_cache: bool = True,
    **kwargs
) -> pd.DataFrame:
    """
    Load a dataset by name as a pandas DataFrame.
    
    Parameters
    ----------
    dataset_name : str
        Name of the dataset (use list_datasets() to see available names).
    use_cache : bool, optional
        Whether to use a local cache (default True).
    **kwargs
        Additional keyword arguments passed to pandas.read_csv().
    
    Returns
    -------
    pd.DataFrame
        The requested dataset as a pandas DataFrame.
    
    Raises
    ------
    ValueError
        If the dataset name is not found in the registry.
    requests.HTTPError
        If the dataset URL is not accessible.
    
    Examples
    --------
    >>> import latamdata as ld
    >>> df = ld.load("alzheimer-latam")
    >>> print(df.head())
    """
    if dataset_name not in _REGISTRY:
        available = list(_REGISTRY.keys())
        raise ValueError(
            f"Dataset '{dataset_name}' not found.\n"
            f"Use latamdata.list_datasets() to see available datasets.\n"
            f"Available: {available}"
        )
    
    meta = _REGISTRY[dataset_name]
    url = meta["url"]
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        from io import StringIO
        df = pd.read_csv(StringIO(response.text), **kwargs)
        return df
    except requests.exceptions.HTTPError as e:
        raise requests.HTTPError(
            f"Could not load dataset '{dataset_name}' from {url}.\n"
            f"The dataset file may not exist yet at this URL.\n"
            f"Original error: {e}"
        )
    except Exception as e:
        raise RuntimeError(
            f"Unexpected error loading dataset '{dataset_name}': {e}\n"
            f"Please report this issue at: https://github.com/juanmoisesd/latamdata-py/issues"
        )
