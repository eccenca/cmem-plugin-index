"""plugin info"""

from dataclasses import asdict, dataclass
from functools import cache

import loguru
import requests
from bs4 import BeautifulSoup


@dataclass
class PackageDetails:
    """Package details"""

    id: str
    name: str
    summary: str
    latest_version: str
    latest_version_time: str


@cache
def get_package_names() -> list[str]:
    """Get all pypi.org package names"""
    url = "https://pypi.org/simple/"
    loguru.logger.info("Start fetching plugin names from pypi.org")
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    # Extract package names
    plugin_list = [a.text for a in soup.find_all("a")]
    loguru.logger.info(f"Got {len(plugin_list)} package names from pypi.org")
    return plugin_list


def get_package_names_with_prefix(prefix: str, ignore: list[str]) -> list[str]:
    """Fetch list of package names from pypi.org"""
    all_names = get_package_names()
    plugin_list = [name for name in all_names if name.startswith(prefix) and name not in ignore]
    loguru.logger.info(
        f"Found {len(plugin_list)} packages with prefix '{prefix}' (ignoring {ignore!s})"
    )
    return plugin_list


def get_package_details(package_id: str) -> PackageDetails | None:
    """Fetch details for a single package from pypi.org"""
    try:
        url = f"https://pypi.org/pypi/{package_id}/json"
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        data = response.json()
        info = data["info"]
        latest_version = info["version"]

        # Fetch the upload time for the latest version
        latest_version_info = data["releases"][latest_version][0]
        upload_time = latest_version_info.get("upload_time", "No upload time available")

        return PackageDetails(
            id=package_id,
            name=info["name"],
            summary=info["summary"] or "No summary available",  # Use summary or default message
            latest_version=latest_version,
            latest_version_time=upload_time,  # Add latest version publish time
        )
    except requests.RequestException as e:
        loguru.logger.exception(e)
        return None


def fetch_all_details(prefix: str, ignore: list[str]) -> list[dict]:
    """Fetch plugin details"""
    plugin_info_list = []
    for package in get_package_names_with_prefix(prefix=prefix, ignore=ignore):
        package_info = get_package_details(package)
        if not package_info:
            loguru.logger.warning(f"No package info available for package '{package}'.")
            continue
        if "rc" in package_info.latest_version:
            loguru.logger.warning(
                f"Package '{package}' ignored since latest version still "
                f"an release candidate: '{package_info.latest_version}'."
            )
            continue
        plugin_info_list.append(asdict(package_info))
        loguru.logger.info(f"Package '{package}' in version {package_info.latest_version} added.")

    return plugin_info_list
