#!/usr/bin/env python

import re
import subprocess
from typing import Optional

import httpx
from importlib_metadata import PackageNotFoundError, version


def get_package_latest_version(package_name: str) -> str:
    """Get the latest stable version of a PyPI package."""
    response = httpx.get(f"https://pypi.org/pypi/{package_name}/json")
    latest_version: str = response.json()["info"]["version"]
    return latest_version


def get_package_local_version(package_name: str) -> Optional[str]:
    """Get the version of a locally installed package."""
    try:
        return str(version(package_name))  # type: ignore[no-untyped-call]
    except PackageNotFoundError:
        return None


if __name__ == "__main__":
    filename = ".pre-commit-config.yaml"
    with open(filename) as file:
        text = file.read()
    for match in re.findall(r"[\w-]+==[\d\w.]+", text):
        package_name, current_version = match.split("==")
        local_version = get_package_local_version(package_name)
        latest_version = get_package_latest_version(package_name)
        text = re.sub(
            f"{package_name}=={current_version}",
            f"{package_name}=={local_version or latest_version}",
            text,
        )
    with open(filename, "w") as file:
        file.write(text)
    subprocess.run(["poetry", "run", "pre-commit", "autoupdate"])
