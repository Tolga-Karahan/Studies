import pytest


def test_external_fixture(conftest_fixture):
    assert "Conftest Fixture" == conftest_fixture
