# Agent guidance

`welog` is a Python application packaged with Docker. Its Python entry point is `welog.py`.

## Development

- Review `requirements.txt` and `Dockerfile` when changing runtime dependencies or packaging.
- Use `python -m compileall welog.py` for a syntax check; no repository test suite is present.
- Use synthetic data when validating behavior, and keep credentials and private infrastructure details out of logs and examples.

## CI

- Before changing GitHub Actions, inspect the current guidance in `pschmitt/ci-workflows`. Use `@main` in every `uses:` reference to a shared workflow or action.
