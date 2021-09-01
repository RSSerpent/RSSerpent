#!/usr/bin/env python
# noqa: T001

import os
import re

import httpx


# Update .pre-commit-config.yaml
pre_commit_config = ".pre-commit-config.yaml"

print(f"Updating {pre_commit_config}")


def get_package_latest_version(package_name: str) -> str:
    """Get the latest stable version of a PyPI package."""
    response = httpx.get(f"https://pypi.org/pypi/{package_name}/json")
    latest_version: str = response.json()["info"]["version"]
    return latest_version


with open(pre_commit_config) as file:
    text = file.read()

for match in re.findall(r"[\w-]+==[\d\w.]+", text):
    package_name, current_version = match.split("==")
    latest_version = get_package_latest_version(package_name)
    if current_version != latest_version:
        print(f"{package_name} {current_version} --> {latest_version}")
        text = re.sub(
            f"{package_name}=={current_version}",
            f"{package_name}=={latest_version}",
            text,
        )

with open(pre_commit_config, "w") as file:
    file.write(text)


# Update poetry dependencies
os.system("poetry update")
os.system("poetry show -lo")
