import pytest

# fixtures defined in conftest.py is available
# across whole directory scope and in subpackages.
# No need for the import
@pytest.fixture
def conftest_fixture():
    return "Conftest Fixture"


# request fixture can be used to introspect
# requesting test function, class or module
@pytest.fixture
def introspect_test_context(request):
    module_list = getattr(request.module, "MODULE_LIST")
    module_list.append("introspection")
