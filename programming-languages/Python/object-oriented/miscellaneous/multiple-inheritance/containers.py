from __future__ import annotations


class ContactList(list["Contact"]):
    def search(self, name: str) -> list["Contact"]:
        """Return all Contacts which contains
        the name specified in name argument.

        Args:
            name (str): Name.

        Returns:
            list[Contact]: A list of Contacts
        which contains the name specified in
        name argument.
        """
        matching_contacts: list["Contact"] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts
