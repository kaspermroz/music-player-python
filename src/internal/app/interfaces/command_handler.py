from abc import ABC


class CommandHandler(ABC):
    """
    CommandHandler is an abstract class which enforces command interface
    """

    def HandlerName(self) -> str:
        return ""

    def Handle(self):
        return NotImplementedError()
