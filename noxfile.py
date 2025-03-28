"""Nox sessions."""

import nox


@nox.session
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
