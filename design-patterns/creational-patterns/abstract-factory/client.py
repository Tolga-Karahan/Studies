import os
import sys

from factory import AbstractFactory, MacOSFactory, WindowsFactory


def create_ui(factory: AbstractFactory) -> None:
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.render()
    checkbox.render()


if __name__ == "__main__":
    env = os.getenv("env", "MacOS")

    if env == "MacOS":
        factory = MacOSFactory()
    elif env == "Windows":
        factory = WindowsFactory()
    else:
        print("Unsupported environment!")
        sys.exit()

    create_ui(factory)
