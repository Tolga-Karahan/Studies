# In testing, fixtures are defined, consistent contexts
# for tests. Contexts set up by fixtures accessed via
# parameters in test functions. Parameters are named
# after the fixture.
#
# PyTest tires to put all fixtures in a linear order.
# In case a fixture is failed, PyTest stops executing
# other fixtures for the test, and mark the test as
# failed.
import os
import tempfile
import pytest
import smtplib

MODULE_LIST = []


class Person:
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other: str):
        return self.name == other


# autouse makes it requested by all tests automatically
@pytest.fixture(autouse=True)
def my_person():
    return Person("Tolga")


# Fixtures can use other fixtures as well
@pytest.fixture
def my_persons(my_person):
    return [Person("RandomGuy"), my_person]


def test_person(my_person, my_persons):
    assert my_person in my_persons


def read_data():
    with open("test_data.txt", "r") as f:
        return f.read().split("\n")[:-1]


# request is builtin fixture which provides
# information on executing function. Fixture
# is called for each parameter value, and
# test is executed for each parameter value
@pytest.fixture(params=read_data())
def data(request):
    yield request.param


def test_data(data):
    assert f"line" == data


# request fixture can be used to introspect
# requesting test function, class or module
def test_introspection(introspect_test_context):
    assert MODULE_LIST == ["introspection"]


# fixtures defined in conftest.py is available
# across whole directory scope and in subpackages.
# No need for the import
def test_external_fixture(conftest_fixture):
    assert "Conftest Fixture" == conftest_fixture


# Time consuming resources such as opening
# a connection can be used in module scope,
# so that each test uses same connection
@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("notpresent@gmail.com", 587, timeout=5)


# Value returned from fixture is cached if
# multiple requests are made to same fixture
# in the same test
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order():
    return []


# Act
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(append_first, order, first_entry):
    # Assert
    assert order == [first_entry]


# We can use usefixtures mark as well to make
# a fixture executed before tests are executed
@pytest.fixture()
def cleandir():
    with tempfile.TemporaryDirectory() as newpath:
        old_cwd = os.getcwd()
        os.chdir(newpath)
        yield
        os.chdir(old_cwd)


@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("testfile", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []


#####################TEARDOWN/CLEANUP####################

# PyTest relies on yield statements to tear down
# fixtures. When execution order is determined,
# each fixture yields in the determined order.
# After tests are finished, clean up code is
# executed after yield statements in fixtures
# in reverse order.
class MailAdminClient:
    def create_user(self):
        return MailUser()

    def delete_user(self, user):
        # do some cleanup
        pass


class MailUser:
    def __init__(self):
        self.inbox = []

    def send_email(self, email, other):
        other.inbox.append(email)

    def clear_mailbox(self):
        self.inbox.clear()


class Email:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body


@pytest.fixture
def mail_admin():
    return MailAdminClient()


@pytest.fixture
def sending_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    mail_admin.delete_user(user)


@pytest.fixture
def receiving_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    mail_admin.delete_user(user)


@pytest.fixture
def email(sending_user, receiving_user):
    _email = Email(subject="Hey!", body="How's it going?")
    sending_user.send_email(_email, receiving_user)
    yield _email
    receiving_user.clear_mailbox()


def test_email_received(sending_user, receiving_user, email):
    assert email in receiving_user.inbox


#####################TEARDOWN/CLEANUP####################
