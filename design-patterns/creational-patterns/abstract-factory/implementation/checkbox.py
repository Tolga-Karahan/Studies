from abc import ABC, abstractmethod


class CheckBox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class MacOSCheckBox(CheckBox):
    def render(self) -> str:
        print("MacOS CheckBox")


class WindowsCheckBox(CheckBox):
    def render(self) -> str:
        print("Windows CheckBox")
