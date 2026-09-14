"""Fixtures: a synthetic repository the tests run against instead of docs/.

Tests never assert against the real corpus, so editing documentation cannot break the suite. The
one exception is `test_engine_names_no_domain`, which deliberately reads the live repository to
discover the names it must guard.
"""

from __future__ import annotations

import pathlib
import shutil

import pytest

FIXTURE_ROOT = pathlib.Path(__file__).parent / "fixtures" / "example-repo"
REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]


@pytest.fixture
def example_repo(tmp_path):
    """A complete, protocol-valid repository with one domain (`example`)."""
    target = tmp_path / "repo"
    shutil.copytree(FIXTURE_ROOT, target)
    return target


@pytest.fixture
def repo_root():
    return REPO_ROOT
