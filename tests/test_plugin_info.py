"""Test index"""

import json
from pathlib import Path

from click.testing import CliRunner

from cmem_plugin_index.cli import cli
from cmem_plugin_index.plugin_info import fetch_all_details, get_package_details

KNOWN_NR_OF_PLUGIN_PACKAGES = 20


def test_get_plugin_details() -> None:
    """Test get_plugin_details"""
    assert get_package_details(package_id="cmem-plugin-index") is None
    details = get_package_details(package_id="cmem-plugin-python")
    assert details is not None
    assert details["name"] == "cmem-plugin-python"
    assert details["id"] == "cmem-plugin-python"
    assert details["summary"] == "Write ad-hoc transformations and workflow tasks with Python."
    assert details["latest_version"] >= "1.1.0"
    assert details["latest_version_time"] >= "2024-12-05T17:51:11"


def test_fetch_all_details() -> None:
    """Test fetch_all_details"""
    prefix = "cmem-plugin-"
    ignore = ["cmem-plugin-base", "cmem-client"]
    plugin_packages = fetch_all_details(prefix=prefix, ignore=ignore)
    assert len(plugin_packages) >= KNOWN_NR_OF_PLUGIN_PACKAGES
    for details in plugin_packages:
        assert str(details["name"]).startswith(prefix)
        assert str(details["id"]).startswith(prefix)
        assert len(str(details["summary"])) > 0
        assert details["latest_version"] > "0.0.0"
        assert details["latest_version_time"] >= "2020-01-01T00:00:00"


def test_cli(tmpdir: Path) -> None:
    """Test cli"""
    output = tmpdir / "output.json"
    result = CliRunner(mix_stderr=False).invoke(cli, [str(output)])
    assert result.exit_code == 0
    json_output = json.loads(output.read_text(encoding="utf-8"))
    assert len(json_output) >= KNOWN_NR_OF_PLUGIN_PACKAGES
