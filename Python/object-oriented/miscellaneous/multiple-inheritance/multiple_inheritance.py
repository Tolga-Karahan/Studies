# Multiple inheritance is what generally we should avoid, but there are
# some cases it can be useful such as mixin classes. They are for adding
# extra functionality to different classes.

from __future__ import annotations
from containers import ContactList
from typing import Protocol

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
    def send_mailn(self, message: str) -> None:
        print(f"Sending mail to {self.email}")


class Contact:
    contacts = ContactList()

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        Contact.contacts.append(self)

    def __repr__(self):
        return f"Contact({self.name}, {self.email})"


class EmailableContact(Contact, MailSender):
    def __init__(self, name: str, email: str):
        super().__init__(name, email)

    def __repr__(self):
        return f"EmailableContact({self.name}, {self.email})"


class Friend(EmailableContact):
    def __init__(self, name: str, email: str, phone: str):
        super().__init__(name, email)
        self.phone = phone

    def __repr__(self):
        return f"Friend({self.name}, {self.email}, {self.phone})"


o1 = Friend("Tolga", "tolga@karahan.com", "0000000")
print(o1.contacts)
