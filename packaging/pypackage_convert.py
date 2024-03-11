"""Generates resources json on pip requirements."""

#!/usr/bin/env python # noqa: E265

# pylint: disable=import-error
import json
import requests
# pylint: enable=import-error


def generate_resource_blocks(requirements_file="requirements.txt"):
    """Main logic to convert."""

    pypi_base_url = "https://pypi.org/pypi"

    resource_blocks = []

    with open(requirements_file, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if line.startswith("-e") or line.startswith("#") or line == "":
                continue

            try:
                pkg_name, version = line.split("==")
            except ValueError:
                print(f"Skipping invalid line: {line}")
                continue

            pkg_info_url = f"{pypi_base_url}/{pkg_name}/{version}/json"
            response = requests.get(pkg_info_url)

            if response.status_code != 200:
                print(
                    f"Failed to fetch package \
                    info for {pkg_name}=={version}"
                )
                continue

            pkg_info = response.json()
            # Select the tar.gz distribution URL
            selected_url = next(
                (
                    url_info
                    for url_info in pkg_info["urls"]
                    if url_info["url"].endswith(".tar.gz")
                ),
                None,
            )

            if not selected_url:
                print(
                    f"No .tar.gz distribution \
                    found for {pkg_name}=={version}"
                )
                continue

            download_url = selected_url["url"]
            sha256 = selected_url["digests"]["sha256"]

            resource_block = {
                "name": f"{pkg_name}",
                "url": f"{download_url}",
                "sha": f"{sha256}",
            }

            resource_blocks.append(resource_block)

    return resource_blocks


if __name__ == "__main__":
    resources_text = generate_resource_blocks()

    final_json = {"resources": resources_text}
    print(json.dumps(final_json))
