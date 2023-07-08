from computer import Computer
from pc import PC
from server import Server


def computer_factory(computer_type: str, **kwargs) -> Computer:
    if computer_type.lower() == "pc":
        return PC(**kwargs)
    elif computer_type.lower() == "server":
        return Server(**kwargs)
