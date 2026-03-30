"""
latamdata-py: One-line access to 38+ open research datasets from Latin America.

Author: Juan Moisés de la Serna Tuya
ORCID: https://orcid.org/0000-0002-8401-8018
Affiliation: Universidad Internacional de La Rioja (UNIR)
License: CC0 1.0 Universal
GitHub: https://github.com/juanmoisesd/latamdata-py
"""

__version__ = "1.0.0"
__author__ = "Juan Moisés de la Serna Tuya"
__email__ = "jmsernatuya@gmail.com"
__license__ = "CC0-1.0"
__orcid__ = "0000-0002-8401-8018"

from .datasets import load, list_datasets, info

__all__ = ["load", "list_datasets", "info", "__version__"]
