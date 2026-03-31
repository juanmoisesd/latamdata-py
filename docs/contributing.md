# Contributing

Thank you for considering a contribution to **latamdata-py**!
We welcome bug reports, feature requests, documentation improvements, and code contributions.

## Ways to Contribute

### 🐛 Report a Bug
[Open a bug report](https://github.com/juanmoisesd/latamdata-py/issues/new?template=bug_report.md)

### 💡 Request a Feature
[Open a feature request](https://github.com/juanmoisesd/latamdata-py/issues/new?template=feature_request.md)

### 📖 Improve Documentation
Documentation lives in the `docs/` directory. Edit any `.md` file and submit a pull request.

### 🧑‍💻 Submit Code

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/latamdata-py.git
   cd latamdata-py
   ```
3. **Set up** the development environment:
   ```bash
   pip install -e ".[dev]"
   pre-commit install
   ```
4. **Create a branch** for your changes:
   ```bash
   git checkout -b feat/my-new-feature
   ```
5. **Make your changes** and run tests:
   ```bash
   pytest tests/ -v
   ```
6. **Commit** following [Conventional Commits](https://www.conventionalcommits.org/):
   ```bash
   git commit -m "feat: add support for filtering by year range"
   ```
7. **Push** and open a Pull Request

## Code Standards

- **Style**: [Black](https://black.readthedocs.io/) (auto-formatted)
- **Linting**: [Ruff](https://docs.astral.sh/ruff/)
- **Type hints**: Required for all public functions
- **Docstrings**: Google style
- **Tests**: Pytest — maintain ≥70% coverage

Run all checks locally:
```bash
black latamdata/ tests/
ruff latamdata/ tests/
mypy latamdata/
pytest --cov=latamdata tests/
```

## Adding a New Dataset

To add a new dataset to the catalog:

1. Add an entry to `latamdata/datasets.py`
2. Include metadata: id, title, doi, url, license, description, coverage
3. Add a row to `docs/datasets/catalog.md`
4. Add at least one integration test in `tests/test_latamdata.py`

## Code of Conduct

All contributors are expected to follow our [Code of Conduct](https://github.com/juanmoisesd/latamdata-py/blob/main/CODE_OF_CONDUCT.md).

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](https://github.com/juanmoisesd/latamdata-py/blob/main/LICENSE).
