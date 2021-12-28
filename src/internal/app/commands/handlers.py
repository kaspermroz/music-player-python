from typing import List, Type

from src.internal.app.commands.say_hi import SayHiHandler
from src.internal.app.interfaces.command_handler import CommandHandler


Handlers: List[Type[CommandHandler]] = [
    SayHiHandler
]
