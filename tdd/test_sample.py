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
