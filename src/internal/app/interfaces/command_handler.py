from abc import ABC


class CommandHandler(ABC):
    """
    CommandHandler is an abstract class which enforces command interface
    """
    def __init__(self, **_kwargs):
        pass

    def HandlerName(self) -> str:
        return ""

    def Handle(self, *_args, **_kwargs):
        return NotImplementedError()
