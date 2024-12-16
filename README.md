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

- `cmem_plugin_index//`: Contains the Python package, a CLI that queries PyPI and fetches details of plugins.
- `data/`: Stores the generated JSON file (`plugins_info.json`) with details about each `cmem-plugin` package, including the package ID, name, summary, and latest version.
- `.github/`: Contains GitHub Actions workflow files that automate the daily updates.
- `README.md`: This file.

## How It Works

1. **GitHub Action**: The `update_plugins.yml` workflow in the `.github/workflows/` directory runs daily to fetch the list of `cmem-plugin` packages from pypi.org and saves the information into a `plugins_info.json` file in the `data/` folder.

2. **Plugin Information**: The script fetches the following details for each plugin:
   - **ID**: The package name.
   - **Name**: The display name of the package.
   - **Summary**: A brief description of the package (if available).
   - **Latest Version**: The latest version available for the package.
   - **Latest Version Publish Time**: The timestamp when the latest version was uploaded to PyPI.

3. **Data Output**: The generated `plugins_info.json` file is stored in the `data/` folder and contains the details of all the plugins.

## Manual Triggering

You can manually trigger the GitHub Action by going to the **Actions** tab of this repository and selecting the **Update CMEM Plugin List** workflow. From there, you can click the **Run workflow** button.

You can also use the command line directly:

```
$ poetry install
Installing dependencies from lock file
...

$ poetry run cmem-plugin-index --help
Usage: cmem-plugin-index [OPTIONS] OUTPUT_FILE

  Fetch and save a list of plugin details from pypi.org

Options:
  --prefix TEXT  Prefix of the packages to fetch.  [default: cmem-plugin-]
  --ignore TEXT  Ignore given packages.  [default: cmem-plugin-base, cmem-
                 client]
  --help         Show this message and exit.

$ poetry run cmem-plugin-index data/plugins_info.json
2024-12-16 16:47:38.499 | WARNING  | cmem_plugin_index.cli:cli:28 - Output file data/plugins_info.json exists, will overwrite it
2024-12-16 16:47:38.499 | INFO     | cmem_plugin_index.plugin_info:get_package_names:14 - Start fetching plugin names from pypi.org
2024-12-16 16:47:47.319 | INFO     | cmem_plugin_index.plugin_info:get_package_names:20 - Got 593112 package names from pypi.org
2024-12-16 16:47:47.348 | INFO     | cmem_plugin_index.plugin_info:get_package_names_with_prefix:28 - Found 25 packages with prefix 'cmem-plugin-' (ignoring ('cmem-plugin-base', 'cmem-client'))
2024-12-16 16:47:51.984 | INFO     | cmem_plugin_index.cli:cli:39 - Data saved to data/plugins_info.json
```

Be aware that cmemc itself fetches the information from [download.eccenca.com](https://download.eccenca.com/cmem-plugin-index/cmem-plugin-index.json).
Uploading the JSON dataset to this host is part of the github action mentioned above.


[poetry-link]: https://python-poetry.org/
[poetry-shield]: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json
[ruff-link]: https://docs.astral.sh/ruff/
[ruff-shield]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&label=Code%20Style
[mypy-link]: https://mypy-lang.org/
[mypy-shield]: https://www.mypy-lang.org/static/mypy_badge.svg
[copier]: https://copier.readthedocs.io/
[copier-shield]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-purple.json

