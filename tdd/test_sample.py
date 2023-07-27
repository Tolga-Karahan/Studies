import pytest


class TestCases:
    value = 5

    def func(self, x):
        return x + 1

    # Each test gets its own instance of the class
    def test_answer(self):
        self.value = 3
        assert self.func(self.value) == 4

    # pytest.mark is used to set metadata on test
    # functions. Custom mark is registered in
    # pyproject.toml file
    @pytest.mark.test
    def test_string(self):
        assert self.value == 5

    # We can parametrize tests so that it can
    # test on different inputs
    @pytest.mark.parametrize("val, res", [(1, 2), (2, 3)])
    def test_func(self, val, res):
        assert res == self.func(val)


# We can parametrize in module or class level as well
@pytest.mark.parametrize(
    "arg1, arg2, res",
    [(1, 2, 3), (2, 3, 5), pytest.param(4, 5, 8, marks=pytest.mark.xfail)],
)
class TestParametrization:
    def add(self, arg1, arg2):
        return arg1 + arg2

    def add2(self, arg1, arg2):
        return arg1 * 1 + arg2

    def test_add(self, arg1, arg2, res):
        assert res == self.add(arg1, arg2)

    def test_add2(self, arg1, arg2, res):
        assert res == self.add2(arg1, arg2)


# We can test cross products of parameters by
# using parametrize decorater multiple times
@pytest.mark.parametrize("arg1", [1, 2])
@pytest.mark.parametrize("arg2, res", [(3, 3), (3, 6)])
class TestCrossProduct:
    def product(self, arg1, arg2):
        return arg1 * arg2

    def test_product(self, arg1, arg2, res):
        assert res == self.product(arg1, arg2)
