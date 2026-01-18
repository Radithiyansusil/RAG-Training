# Repository Guidelines

## Project Structure & Module Organization
This repository is currently small and flat. The root contains the entry script `5_tick.py` and a brief `README.md`. A local virtual environment may live in `.venv/` and is ignored by git. If you add more code, group modules by domain under a new folder (for example, `src/` or `rag/`) and keep top-level files limited to documentation and entry points.

## Build, Test, and Development Commands
No build system or task runner is configured. Run code directly with Python:

```powershell
python 5_tick.py
```

If you rely on a local virtual environment, activate it before running scripts (for example, `./.venv/Scripts/Activate.ps1` on Windows). Add a `requirements.txt` or `pyproject.toml` when dependencies grow beyond a few ad-hoc installs.

## Coding Style & Naming Conventions
Use standard Python conventions: 4-space indentation, `snake_case` for functions/variables, and `PascalCase` for classes. Keep filenames short and descriptive (for example, `pdf_loader.py`). No formatter or linter is configured yet; keep code PEP 8 compliant and add tooling only if the project expands.

## Testing Guidelines
There are no tests in the repository. If you introduce tests, place them under `tests/` and use `test_*.py` naming so common runners can discover them. Document how to run tests in `README.md` once a framework is added.

## Commit & Pull Request Guidelines
Git history only includes a single “Initial commit”, so no established message pattern exists. Use concise, imperative commit summaries (for example, “Add PDF loader script”). For pull requests, include a short description, list how you verified changes (commands run), and link any related issues or course tasks.
