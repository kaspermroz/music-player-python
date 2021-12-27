from typing import List

from internal.app.commands.say_hi import SayHiHandler
from internal.app.command_handler import CommandHandler


Handlers: List[CommandHandler] = [
    SayHiHandler
]
