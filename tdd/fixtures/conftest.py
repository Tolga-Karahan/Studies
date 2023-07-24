import pytest


@pytest.fixture
def conftest_fixture():
    return "Conftest Fixture"


@pytest.fixture
def introspect_test_context(request):
    module_list = getattr(request.module, "MODULE_LIST")
    module_list.append("introspection")
