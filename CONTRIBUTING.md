# How to contribute

Everyone is free to contribute on this project.

There are two ways to contribute:

- [Submit an issue](https://github.com/angryfoxx/pytest_httpx2/issues/new/choose).
- [Submit a pull request](https://github.com/angryfoxx/pytest_httpx2/compare).

## Submitting an issue

Before creating an issue please make sure that it was not already reported.

### When?

- You encountered an issue.
- You have a change proposal.
- You have a feature request.

### How?

1) Go to the *Issues* tab and click on the *New issue* button.
2) Title should be a small sentence describing the request.
3) The comment should contain as much information as possible
    * Actual behavior (including the version you used)
    * Expected behavior
    * Steps to reproduce

## Submitting a pull request

### When?

- You fixed an issue.
- You changed something.
- You added a new feature.

### How?

#### Code

1) Create a new branch based on `develop` branch.
2) Install [uv](https://docs.astral.sh/uv/) and sync dependencies:
    ```shell
    uv sync --all-extras --dev
    ```
3) Ensure tests pass:
    ```shell
    uv run pytest
    ```
4) Install [pre-commit](https://pre-commit.com) hooks (uses [Tombi](https://tombi-toml.github.io/tombi/) for TOML formatting and linting, [Ruff](https://docs.astral.sh/ruff/) for Python linting/formatting, and [ty](https://docs.astral.sh/ty/) for type checking):
    ```shell
    uv run pre-commit install
    ```
5) Add your changes.
6) Add at least one [`pytest`](https://doc.pytest.org/en/latest/index.html) test case.
    * Unless it is an internal refactoring request or a documentation update.
7) Add related [changelog entry](https://keepachangelog.com/en/1.1.0/) in the `Unreleased` section.
    * Unless it is a documentation update.

## Releasing

Maintainers: see [RELEASING.md](RELEASING.md) for PyPI trusted publishing and tag workflow.

#### Enter pull request

1) Go to the [*Pull requests* tab](https://github.com/angryfoxx/pytest_httpx2/pulls) and click on the [*New pull request* button](https://github.com/angryfoxx/pytest_httpx2/compare).
2) *base* should always be set to `develop` and it should be compared to your branch.
3) Title should be a small sentence describing the request.
4) The comment should contain as much information as possible
    * Actual behavior (before the new code)
    * Expected behavior (with the new code)
    * Steps to reproduce (with and without the new code to see the difference)
