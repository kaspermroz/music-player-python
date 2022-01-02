from typing import List

from src.internal.app.interfaces.command_handler import CommandHandler
from src.internal.app.commands.handlers import Handlers
from src.internal.domain.music.library import Library
from src.internal.adapters.local_player import LocalPlayer


def CommandHandlers() -> List[CommandHandler]:
    handlers: List[CommandHandler] = []
    handlerDeps = {
        "library": Library(),
        "local_player": LocalPlayer(),
    }

    for h in Handlers:
        handler = h(**handlerDeps)
        handlers.append(handler)

    return handlers
