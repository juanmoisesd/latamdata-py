# Contributing to latamdata-py

Thank you for your interest in contributing! 🐍

## Development Setup

```bash
git clone https://github.com/juanmoisesd/latamdata-py.git
cd latamdata-py
pip install -e ".[dev]"
pre-commit install
```

## Ways to Contribute

### 🗃️ Add a Dataset
- Open a [feature request](../../issues/new?template=feature_request.md)
- Include: dataset name, source URL, DOI, description, and sample access code

### 🐛 Report a Bug
- Use the [bug report template](../../issues/new?template=bug_report.md)
- Include Python version, OS, and steps to reproduce

### 💻 Code Contributions
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/add-new-dataset`
3. Write tests in `tests/`
4. Ensure `pytest` and `flake8` pass
5. Open a Pull Request

## Code Style
- Format with **black**: `black .`
- Lint with **flake8**: `flake8 .`
- Sort imports with **isort**: `isort .`
- Pre-commit hooks handle this automatically

## Running Tests
```bash
pytest tests/ -v
```

## Code of Conduct
See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Citation
See [CITATION.cff](CITATION.cff).
