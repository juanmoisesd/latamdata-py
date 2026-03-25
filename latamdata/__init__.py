"""
latamdata-py: Python package for one-line access to 38 open research datasets from Latin America.

Author: Juan Moisés de la Serna Tuya
ORCID: 0000-0002-8401-8018
License: CC BY 4.0
GitHub: https://github.com/juanmoisesd/latamdata-py
"""

__version__ = "0.1.0"
__author__ = "Juan Moisés de la Serna Tuya"
__license__ = "CC BY 4.0"
__orcid__ = "0000-0002-8401-8018"

from .datasets import (
    load,
    load_many,
    list_all,
    info,
    search,
    load_by_topic,
    export
)

# Convenience aliases
datasets = load

__all__ = [
    "load",
    "load_many",
    "list_all",
    "info",
    "search",
    "load_by_topic",
    "export",
    "__version__",
]
