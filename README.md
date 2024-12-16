# CMEM Plugin Index

This repository contains an up-to-date list of Python packages starting with the prefix `cmem-plugin`, fetched from [PyPI](https://pypi.org). It is updated daily through an automated GitHub Action, which queries the PyPI simple index and gathers details for all plugins starting with `cmem-plugin`.

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

3. **Data Output**: The generated `plugins_info.json` file is stored in the `data/` folder and contains the details of all the plugins.

## Manual Triggering

You can manually trigger the GitHub Action by going to the **Actions** tab of this repository and selecting the **Update CMEM Plugin List** workflow. From there, you can click the **Run workflow** button.

## Folder Structure
