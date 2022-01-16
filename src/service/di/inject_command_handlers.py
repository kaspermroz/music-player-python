from typing import List

from src.internal.app.interfaces.command_handler import CommandHandler
from src.internal.app.commands.handlers import Handlers
from src.internal.domain.music.library import Library
from src.internal.adapters.streaming_player import StreamingPlayer


def CommandHandlers(local_player) -> List[CommandHandler]:
    """
    Returns application command handlers, used for changing state of application
    :param local_player:
    :return:
    """
    handlers: List[CommandHandler] = []
    handlerDeps = {
        "library": Library(),
        "local_player": local_player,
        "streaming_player": StreamingPlayer(),
    }

    for h in Handlers:
        handler = h(**handlerDeps)
        handlers.append(handler)

    return handlers
