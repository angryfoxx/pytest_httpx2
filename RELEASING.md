# Releasing httpx2-pytest on PyPI

Distribution name on PyPI: **httpx2-pytest**
Import name: **pytest_httpx2**

Releases are automated with [release-please](https://github.com/googleapis/release-please).

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

## First release (1.0.0)

Version **1.0.0** is not on PyPI yet. `release-please-config.json` sets `"release-as": "1.0.0"` so the first Release Please PR targets that version. **Remove `release-as` after `v1.0.0` is published**; later releases use conventional commits only.

The manifest (`.release-please-manifest.json`) starts empty so release-please does not treat `1.0.0` as already released.

## How releases work

1. Merge changes into **`master`** using [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `chore:`, etc.).
2. Run the [Release Please workflow](.github/workflows/release-please.yml) on `master` (workflow dispatch only):

   ```shell
   gh workflow run release-please.yml --ref master
   ```

   It opens or updates a release PR that bumps `pytest_httpx2/version.py`, `CHANGELOG.md`, and `.release-please-manifest.json`.
3. Review and merge the release PR on `master`.
4. Release Please creates a GitHub release and tag (for example `v1.1.0`).
5. The [Release workflow](.github/workflows/release.yml) runs on `release: published`, builds the sdist/wheel, runs `twine check`, and publishes with `uv publish`.
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
