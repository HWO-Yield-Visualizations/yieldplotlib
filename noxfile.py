"""Nox sessions."""

import nox

PYTHON_VERSIONS = ["3.9", "3.10", "3.11", "3.12"]


@nox.session(python=PYTHON_VERSIONS)
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
