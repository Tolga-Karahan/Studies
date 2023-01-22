# Multiple inheritance is what generally we
# should avoid, but there are some cases it
# can be useful such as mixin classes. They
# are for adding extra functionality to
# different classes.

from __future__ import annotations
from typing import Any, Protocol

from address_holder import AddressHolder
from containers import ContactList

# A protocol class specifies an interface.
# In this case, it is used to describe host
# classes for our mixin classes. Thanks to
# Python's duck typing, there is no need to
# explicitly inheriting this Protocol class,
# but it is better in terms of readability.
# Duck typing means, type is determined by
# behaviours and properties instead of
# explicit type of the object. If it walks
# like a duck and its quacks like a duck,
# then it must be a duck.
class Emailable(Protocol):
    email: str


# Our mixin class for sending mail to
# itself. It works with Emailable classes
# which have a string email attribute.
class MailSender(Emailable):
    def send_mail(self, message: str) -> None:
        print(f"Sending mail to {self.email}")


class Contact:
    contacts = ContactList()

    def __init__(self, name: str, email: str, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.contacts.append(self)

    def __repr__(self):
        return f"Contact({self.name}, {self.email})"

class Friend(Contact, MailSender, AddressHolder):
    # '/' special parameter can be put between
    # positional and keyword argument to separate
    # them.
    def __init__(self, /, phone: str, **kwargs: Any) -> None:
        """super() follows method resoulution order but
        __init__ methods of different classes expects
        different parameters. It poses a question: how
        parameters can be provided in a way that they
        are consumed through __init__ calls in method
        resolution order. The answer is using kwargs.
        In this way each __init__ method will get the
        parameters they require. One caveat is now
        because arguments to other __init__ methods
        are absracted out in kwargs, complete list
        of arguments are not apparent for users.
        These arguments should be stated in docstring
        to make it apparent for users. In general, 
        composition should be preferred over 
        inheritance.

        Args:
            phone (str): Phone number.
            name (str): Name.
            email (str): Email address.
            street (str): Street name.
            city (str): City name.
            state (str): State name.
            code (str): Code of the place.
        """
    
        super().__init__(**kwargs)
        self.phone = phone

    def __repr__(self):
        return f"Friend({self.name}, {self.email}, {self.phone})"


o1 = Friend(
    name="Tolga",
    email="tolga@karahan.com",
    phone="0000000",
    street="fake_street",
    city="fake_city",
    state="fake_state",
    code="fake_code"
)
print(o1.contacts)
o1.send_mail("Hey")
print(Friend.__mro__)