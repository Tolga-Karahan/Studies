from datetime import datetime

import objects
from objects import (
    DBEngine,
    double_constant,
    Employee,
    get_environment,
    get_time_of_day,
)

import pytest


@pytest.mark.parametrize(
    "day, expected",
    [
        (datetime(2016, 5, 20, 0, 0, 0), "Night"),
        (datetime(2016, 5, 20, 1, 10, 0), "Night"),
        (datetime(2016, 5, 20, 6, 10, 0), "Morning"),
        (datetime(2016, 5, 20, 12, 0, 0), "Afternoon"),
        (datetime(2016, 5, 20, 14, 10, 0), "Afternoon"),
        (datetime(2016, 5, 20, 18, 0, 0), "Evening"),
        (datetime(2016, 5, 20, 19, 10, 0), "Evening"),
    ],
)
def test_get_time_of_day(day, expected, mocker):
    # Mock datetime object inside the module
    # that contains code to be tested
    date_mock = mocker.patch("objects.datetime")
    # Mock datetime.now() function used inside
    # the code block to be tested
    date_mock.now.return_value = day
    assert get_time_of_day() == expected


# DB mocking example
def test_engine(mocker):
    connector_mock = mocker.patch("objects.DBConnector.__init__", return_value=None)
    mocker.patch("objects.DBEngine.load_data", return_value="abc")
    engine = DBEngine(
        connector=connector_mock,
    )

    assert "abc" == engine.load_data()


# API call mocking example
def test_monthly_schedule(mocker):
    employee = Employee("Not", "Exist", 5000)
    mocked_request = mocker.patch("objects.requests.get")
    mocked_request.return_value.ok = True
    mocked_request.return_value.text = "Success"

    schedule = employee.monthly_schedule("September")
    mocked_request.assert_called_with("http://company.com/Exist/September")
    assert "Success" == schedule


def test_get_department(mocker):
    employee = Employee("Not", "Exist", 5000)
    mocked_request = mocker.patch("objects.requests.get")
    mocked_request.return_value.status_code = 200
    mocked_request.return_value.json.return_value = {"Departmnet": "IT"}

    response = employee.get_department()
    mocked_request.assert_called_with("http://company.com/Exist/Not")
    assert 200 == response.status_code
    assert {"Departmnet": "IT"} == response.json()


# monkeypatch fixture can be used to mock
# environment related settings
@pytest.mark.parametrize(
    "mocked_environment, expected", [("prod", "prod-env"), ("dev", "dev-env")]
)
def test_get_environment(mocked_environment, expected, monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", mocked_environment)
    assert expected == get_environment()


# We can use pytest.raises context manager
# to test exceptions
def test_get_environment_exception(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "STAGE")

    with pytest.raises(ValueError, match="Unknown Environment"):
        get_environment()


# Mock a constant
def test_double_constant(mocker):
    # Mock the constant
    mocker.patch.object(objects, "SOME_CONSTANT", 5)
    assert 10 == double_constant()
