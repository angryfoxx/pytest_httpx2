# How to contribute

Everyone is free to contribute on this project.

There are two ways to contribute:

- [Submit an issue](https://github.com/angryfoxx/pytest_httpx2/issues/new/choose).
- [Submit a pull request](https://github.com/angryfoxx/pytest_httpx2/compare).

## Submitting an issue

Before creating an issue please make sure that it was not already reported.

Title should be a small sentence describing the request.

## Submitting a pull request

### When?

- You fixed an issue.
- You changed something.
- You added a new feature.

### How?

#### Code

1) Create a new branch based on `master`.
2) Install [uv](https://docs.astral.sh/uv/) and sync dependencies:
    ```shell
    uv sync --all-extras --dev
    ```
3) Ensure tests pass:
    ```shell
    uv run pytest
    ```
4) Install [prek](https://prek.j178.dev) Git hooks (config: [`.pre-commit-config.yaml`](.pre-commit-config.yaml); uses [ryl](https://github.com/owenlamont/ryl) for YAML linting, [Tombi](https://tombi-toml.github.io/tombi/) for TOML formatting and linting, [Ruff](https://docs.astral.sh/ruff/) for Python linting/formatting, and [ty](https://docs.astral.sh/ty/) for type checking):
    ```shell
    prek install --prepare-hooks
    ```
    This installs Git hooks for `pre-commit` and `pre-push`. Run hooks manually with `prek run --all-files` (commit stage) or `prek run --hook-stage pre-push --all-files` before pushing. Update hook revisions with `prek auto-update`.
5) Add your changes.
6) Add at least one [`pytest`](https://doc.pytest.org/en/latest/index.html) test case.
    * Unless it is an internal refactoring request or a documentation update.
7) Use [Conventional Commits](https://www.conventionalcommits.org/) in PR titles and commit messages (`feat:`, `fix:`, `docs:`, `chore:`, etc.). [release-please](https://github.com/googleapis/release-please) updates `CHANGELOG.md` when maintainers merge the release PR on `master`.
    * Breaking changes must use `type(scope)!:` (for example `feat(httpx2)!: …`), not `type!(scope):` — release-please cannot parse the latter.

## Releasing

Maintainers: see [RELEASING.md](RELEASING.md) for release-please and PyPI publishing.

#### Enter pull request

1) Go to the [*Pull requests* tab](https://github.com/angryfoxx/pytest_httpx2/pulls) and click on the [*New pull request* button](https://github.com/angryfoxx/pytest_httpx2/compare).
2) *base* should always be set to `master` and it should be compared to your branch.
3) Title should be a small sentence describing the request.
4) The comment should contain as much information as possible
    * Actual behavior (before the new code)
    * Expected behavior (with the new code)
    * Steps to reproduce (with and without the new code to see the difference)
