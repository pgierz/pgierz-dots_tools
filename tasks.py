#!/usr/bin/env python3
"""
Invoke tasks for this project
"""
from invoke import task


@task
def clean(c):
    """
    Clean up the project
    """
    for pattern in [
        "dist",
        "build",
        "*.egg-info",
        ".pytest_cache",
        ".tox",
        ".mypy_cache",
        ".coverage",
        "__pycache__",
    ]:
        c.run(f"rm -rf {pattern}")
