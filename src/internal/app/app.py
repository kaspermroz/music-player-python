from typing import List, Type

from src.internal.app.interfaces.command_handler import CommandHandler
from src.internal.app.interfaces.configuration import Configuration


class Application:
    SayHi = CommandHandler()
    Config = Configuration()

    def __init__(
            self,
            configuration: Type[Configuration],
            commands: List[Type[CommandHandler]],
    ) -> None:
        self.Config = configuration
        for c in commands:
            handler = c()
            setattr(self, handler.HandlerName(), handler)
