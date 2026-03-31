"""
pytest configuration and shared fixtures for latamdata-py tests.
"""
import pytest


# ---------------------------------------------------------------------------
# Session-scoped fixtures (created once per test run)
# ---------------------------------------------------------------------------

@pytest.fixture(scope="session")
def sample_dataset_id():
    """Return the ID of a lightweight dataset for integration tests."""
    return "alzheimer-latinamerica-dashboard"


@pytest.fixture(scope="session")
def sample_country():
    """Return a valid ISO-3166-1 alpha-2 country code for filter tests."""
    return "CO"


@pytest.fixture(scope="session")
def expected_columns():
    """Columns that every latamdata DataFrame must contain."""
    return ["country", "year", "value"]


# ---------------------------------------------------------------------------
# Function-scoped fixtures (re-created for each test)
# ---------------------------------------------------------------------------

@pytest.fixture()
def mock_dataset_info():
    """Minimal dataset-info dict used for unit tests without network calls."""
    return {
        "id": "test-dataset",
        "title": "Test Dataset",
        "doi": "10.5281/zenodo.0000000",
        "description": "A test dataset.",
        "license": "CC-BY-4.0",
        "version": "1.0.0",
        "coverage": {"countries": ["CO", "MX", "AR"], "years": [2020, 2021, 2022]},
    }


@pytest.fixture()
def mock_empty_dataframe():
    """Return an empty DataFrame with the expected schema."""
    import pandas as pd
    return pd.DataFrame(columns=["country", "year", "value"])


# ---------------------------------------------------------------------------
# Markers
# ---------------------------------------------------------------------------

def pytest_configure(config):
    """Register custom pytest markers."""
    config.addinivalue_line(
        "markers",
        "integration: marks tests that make real network requests (deselect with -m 'not integration')",
    )
    config.addinivalue_line(
        "markers",
        "slow: marks tests that are known to be slow",
    )
