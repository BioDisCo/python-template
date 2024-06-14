# python-template
A template repository for Python development

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![static analysis workflow](https://github.com/BioDisCo/python-template/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/BioDisCo/python-template/actions/workflows/pre-commit.yaml/)
[![test workflow](https://github.com/BioDisCo/python-template/actions/workflows/test.yaml/badge.svg)](https://github.com/BioDisCo/python-template/actions/workflows/test.yaml/)

## First Steps

0. Install `pyenv`:
   ```bash
   curl https://pyenv.run | bash
   ```
   Then install a Python interpreter in `pyenv`:
   ```bash
   pyenv install 3.12
   pyenv global 3.12
   ```
   To allows multi-version testing, install multiple versions, e.g.:
   ```bash
   pyenv install 3.12 3.11 3.10
   pyenv global 3.12 3.11 3.10
   ```

1. Install the development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Install the pre-commit hooks:
   ```bash
   pre-commit install
   ```

3. If your IDE or editor doesn't do it for you, create virtual environment:
   ```bash
   python -m venv venv
   ```
   Then activate it (do this every time you work on the project):
   ```bash
   . venv/bin/activate
   ```
   After you're done, deactivate the virtual environment:
   ```bash
   deactivate
   ```

4. Change `pyproject.toml` to match your needs (in particular project name,
   description, keywords, authors, and maintainers).

5. Change the `multiplier` directory to your project name, write your project
   code, your tests, and your example scripts.

6. Install your package locally:
   ```bash
   pip install -e .
   ```

7. After programming, put all packages you used into the
   `requirements.txt` file:
   ```bash
   pip freeze > requirements.txt
   ```
   Then remove the local package from the file (line starts with `-e`).

8. Test your code:
   ```bash
   tox
   ```

9. Add all new files via `git add`.

10. Do a dry-run of all pre-commit checks:
    ```bash
    pre-commit run --all-files
    ```

11. Commit and push your code, then check result of GitHub actions.
