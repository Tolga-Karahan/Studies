from typing import Any


class AddressHolder:
    def __init__(
        self, street: str, city: str, state: str, code: str, **kwargs: Any
    ) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.code = code

    def __repr__(self):
        return (
            f"AddressHolder("
            + "{self.street},"
            + f"{self.city},"
            + f"{self.state},"
            + f"{self.code})"
        )
