# Makefile for latamdata-py
.PHONY: install dev test lint format clean build docs help

help:
	@echo "Available commands:"
	@echo "  make install   - Install package"
	@echo "  make dev       - Install dev dependencies"
	@echo "  make test      - Run tests"
	@echo "  make lint      - Run linters"
	@echo "  make format    - Format code"
	@echo "  make clean     - Clean build artifacts"
	@echo "  make build     - Build distribution"

install:
	pip install -e .

dev:
	pip install -e ".[dev]"
	pre-commit install

test:
	pytest tests/ -v --cov=latamdata --cov-report=term-missing

lint:
	flake8 . --max-line-length=88 --extend-ignore=E203,W503
	mypy latamdata/ --ignore-missing-imports

format:
	black .
	isort .

clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache .mypy_cache __pycache__
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build

release: build
	twine upload dist/*
