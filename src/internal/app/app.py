from typing import List
from internal.app.commands.handlers import CommandHandler

class Application:
    def __init__(self, commands: List[CommandHandler]) -> None:
        for c in commands:
            setattr(self, c.HandlerName(self), c())