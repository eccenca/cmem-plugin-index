# cmem-plugin-index

Create an up-to-date list of Corporate Memory plugin packages.

This repository contains an up-to-date list of Python packages starting with the prefix `cmem-plugin`, fetched from [PyPI](https://pypi.org).
It is updated daily through an automated GitHub Action, which queries the PyPI simple index and gathers details for all plugins starting with `cmem-plugin`.

[![workflow](https://github.com/eccenca/cmem-plugin-index/actions/workflows/check.yml/badge.svg)](https://github.com/eccenca/cmem-plugin-index/actions)  
[![poetry][poetry-shield]][poetry-link] [![ruff][ruff-shield]][ruff-link] [![mypy][mypy-shield]][mypy-link] [![copier][copier-shield]][copier] 

## Development

- Run [task](https://taskfile.dev/) to see all major development tasks.
- Use [pre-commit](https://pre-commit.com/) to avoid errors before commit.
- This repository was created with [this copier template](https://github.com/eccenca/cmem-plugin-template).

## Repository Structure

- `src/`: Contains the Python script (`plugin_info.py`) that queries PyPI and fetches details of plugins starting with `cmem-plugin`.
- `data/`: Stores the generated JSON file (`plugins_info.json`) with details about each `cmem-plugin` package, including the package ID, name, summary, and latest version.
- `.github/`: Contains GitHub Actions workflow files that automate the daily updates.
- `README.md`: This file.

## How It Works

1. **GitHub Action**: The `update_plugins.yml` workflow in the `.github/workflows/` directory runs daily to fetch the list of `cmem-plugin` packages from PyPI and save the information into a `plugins_info.json` file in the `data/` folder.
   
2. **Plugin Information**: The script fetches the following details for each plugin:
   - **ID**: The package name.
   - **Name**: The display name of the package.
   - **Summary**: A brief description of the package (if available).
   - **Latest Version**: The latest version available for the package.
   - **Latest Version Publish Time**: The timestamp when the latest version was uploaded to PyPI.

3. **Data Output**: The generated `plugins_info.json` file is stored in the `data/` folder and contains the details of all the plugins.

## Manual Triggering

You can manually trigger the GitHub Action by going to the **Actions** tab of this repository and selecting the **Update CMEM Plugin List** workflow. From there, you can click the **Run workflow** button.

[poetry-link]: https://python-poetry.org/
[poetry-shield]: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json
[ruff-link]: https://docs.astral.sh/ruff/
[ruff-shield]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&label=Code%20Style
[mypy-link]: https://mypy-lang.org/
[mypy-shield]: https://www.mypy-lang.org/static/mypy_badge.svg
[copier]: https://copier.readthedocs.io/
[copier-shield]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json

