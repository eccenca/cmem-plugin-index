"""plugin info cli"""

import json
from pathlib import Path

import click
import loguru

from cmem_plugin_index.plugin_info import fetch_all_details

IGNORED_PACKAGES = [
    "cmem-client",  # not a plugin
    "cmem-plugin-base",  # not a plugin
    "cmem-plugin-databus",  # no support
    "cmem-plugin-examples",  # only for testing
    "cmem-plugin-kaggle",  # no support
]


@click.command()
@click.argument("OUTPUT_FILE")
@click.option(
    "--prefix", default="cmem-plugin-", show_default=True, help="Prefix of the packages to fetch."
)
@click.option(
    "--ignore",
    default=IGNORED_PACKAGES,
    show_default=True,
    multiple=True,
    help="Ignore given packages.",
)
def cli(output_file: str, prefix: str, ignore: list[str]) -> None:
    """Fetch and save a list of plugin details from pypi.org"""
    output = Path(output_file)
    if output.exists():
        loguru.logger.warning(f"Output file {output} exists, will overwrite it")

    # Ensure the 'data' directory exists
    if not output.parent.exists():
        loguru.logger.warning(f"Directory {output.parent} doesn't exist, creating it")
        output.parent.mkdir(parents=True)

    plugin_info_list = fetch_all_details(prefix=prefix, ignore=ignore)

    # Save the plugin information to a JSON file in the 'data' folder
    output.write_text(json.dumps(plugin_info_list, indent=4))
    loguru.logger.info(f"Data saved to {output}")
