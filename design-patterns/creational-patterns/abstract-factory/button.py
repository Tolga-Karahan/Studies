from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class MacOSButton(Button):
    def render(self) -> str:
        print("MacOS Button")


class WindowsButton(Button):
    def render(self) -> str:
        print("Windows Button")
