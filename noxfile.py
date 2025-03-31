"""Nox sessions."""

import nox


@nox.session(venv_backend="uv", python=["3.10", "3.11", "3.12", "3.13"])
def tests(session):
    """Run the test suite with pytest."""
    # Install all test dependencies
    session.install(".[test]")
    # Run the tests
    session.run(
        "pytest",
        "tests/",
        "--cov=yieldplotlib",
        "--cov-report=term",
        "--cov-report=html",
        *session.posargs,
    )
