# FastAPI Template

A template for creating new FastAPI webservices. Originally this is intended to be used with the Banter Bus application.
However there is nothing stopping you from using this with other projects.

## Features

- FastAPI web framework
- Docker containersiation technology
- Poetry dependency manager
- Beanie ODM for MongoDB
- Gitlab for CI/CD pipeline
- Google Cloud for deployment
- Makefile for basic commands
- Copier template management
- pre-commit pre git commit hooks
  - Black code formatter
  - Flake linter
  - isort import sorter
  - mypy type checker
- Pytest for testing & coverage

## Usage

```bash
pipx install copier

copier https://gitlab.com/banter-bus/fastapi-template /path/to/project
```
