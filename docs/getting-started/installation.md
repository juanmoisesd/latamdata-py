# Installation

## Requirements

- Python 3.8 or higher
- pip (Python package manager)

## Install from PyPI

The simplest way to install latamdata-py:

```bash
pip install latamdata-py
```

## Install with optional dependencies

For Jupyter notebook support and data visualization:

```bash
pip install "latamdata-py[viz]"
```

For full development environment:

```bash
pip install "latamdata-py[dev]"
```

## Install from source

```bash
git clone https://github.com/juanmoisesd/latamdata-py.git
cd latamdata-py
pip install -e ".[dev]"
```

## Verify installation

```python
import latamdata as ld
print(ld.__version__)
```

## Upgrading

```bash
pip install --upgrade latamdata-py
```

## Troubleshooting

### SSL Certificate errors

If you encounter SSL errors when downloading datasets, try:

```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org latamdata-py
```

### Proxy environments

Set your proxy environment variables before installing:

```bash
export HTTPS_PROXY=http://your-proxy:port
pip install latamdata-py
```
