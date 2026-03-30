"""
Tests for latamdata-py package.
"""

import pytest
import pandas as pd


def test_import():
    """Test that the package imports successfully."""
    import latamdata
    assert latamdata.__version__ == "1.0.0"
    assert latamdata.__author__ == "Juan Moisés de la Serna Tuya"
    assert latamdata.__license__ == "CC0-1.0"


def test_list_datasets():
    """Test that list_datasets returns a DataFrame."""
    import latamdata as ld
    df = ld.list_datasets()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert "name" in df.columns
    assert "title" in df.columns
    assert "doi" in df.columns


def test_info_valid():
    """Test info() with a valid dataset name."""
    import latamdata as ld
    result = ld.info("alzheimer-latam")
    assert isinstance(result, dict)
    assert "title" in result
    assert "url" in result


def test_info_invalid():
    """Test info() raises ValueError for invalid dataset name."""
    import latamdata as ld
    with pytest.raises(ValueError, match="not found"):
        ld.info("nonexistent-dataset")


def test_load_invalid():
    """Test load() raises ValueError for invalid dataset name."""
    import latamdata as ld
    with pytest.raises(ValueError, match="not found"):
        ld.load("nonexistent-dataset")
