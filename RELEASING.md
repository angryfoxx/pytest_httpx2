# Releasing httpx2-pytest on PyPI

Distribution name on PyPI: **httpx2-pytest**
Import name: **pytest_httpx2**

## One-time PyPI setup (trusted publishing)

Configure [PyPI trusted publishers](https://docs.pypi.org/trusted-publishers/) so GitHub Actions can upload releases without API tokens.

### Production PyPI

1. Create the project on [pypi.org](https://pypi.org/) (first upload can also create it via the workflow).
2. Open **httpx2-pytest** → **Publishing** → **Add a new publisher**.
3. Use:

| Field | Value |
| --- | --- |
| PyPI Project Name | `httpx2-pytest` |
| Owner | `angryfoxx` |
| Repository name | `pytest_httpx2` |
| Workflow name | `release.yml` |
| Environment name | `pypi` |

4. In this GitHub repository, create an environment named **`pypi`** (Settings → Environments). No secrets are required when using trusted publishing.

## Version number

Set the release version in `pytest_httpx2/version.py` (`__version__`) before tagging.

## Release checklist

1. Update `CHANGELOG.md` (move **Unreleased** notes under a dated version heading).
2. Bump `pytest_httpx2/version.py`.
3. Commit on `master` (or your release branch).
4. Tag and push:

```shell
git tag v1.0.0
git push origin v1.0.0
```

5. The [Release workflow](.github/workflows/release.yml) builds the sdist/wheel, runs `twine check`, and publishes to PyPI.
6. Confirm the release: https://pypi.org/project/httpx2-pytest/

## Local build verification

```shell
uv sync --dev
uv build
uv run twine check dist/*
```

## User install

```shell
pip install httpx2-pytest
```
