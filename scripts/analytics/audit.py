"""Fail publication if the generated build includes credential material."""

import re

from pathlib import Path

from scripts.analytics.report import read_snapshot

BAD_CONTENT = re.compile(
    rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|"
    rb'"(?:private_key|private_key_id|refresh_token|client_secret|'
    rb'credential_source|subject_token|access_token)"\s*:|'
    rb'"type"\s*:\s*"(?:service_account|external_account|authorized_user)"|'
    rb"ya29\.[A-Za-z0-9_-]{15,}"
)


def audit(directory: Path) -> None:
    """Check the endpoint and every published file before artifact upload."""
    endpoint = directory / "analytics/data.json"
    if not endpoint.is_file():
        raise ValueError("Missing public analytics endpoint")
    read_snapshot(endpoint)
    for path in directory.rglob("*"):
        if path.is_symlink():
            raise ValueError("Symlinks are forbidden in the published build")
        if not path.is_file():
            continue
        if (
            path.name.startswith(("gha-creds-", ".env"))
            or path.suffix in {".pem", ".key", ".p12"}
            or any(
                part in {".git", ".cache", ".venv"}
                for part in path.relative_to(directory).parts
            )
            or BAD_CONTENT.search(path.read_bytes())
        ):
            raise ValueError(f"Potential credential material in {path.name}")


if __name__ == "__main__":
    audit(Path("build"))
    print("Public endpoint validated; build credential audit passed.")
