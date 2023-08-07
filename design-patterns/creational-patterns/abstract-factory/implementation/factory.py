from abc import ABC, abstractmethod

from button import Button, MacOSButton, WindowsButton
from checkbox import CheckBox, MacOSCheckBox, WindowsCheckBox


class AbstractFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass


class MacOSFactory(AbstractFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> CheckBox:
        return MacOSCheckBox()


class WindowsFactory(AbstractFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> CheckBox:
        return WindowsCheckBox()
