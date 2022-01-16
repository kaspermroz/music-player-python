from typing import List

from src.internal.adapters.streaming_player import StreamingPlayer
from src.internal.app.interfaces.query_handler import QueryHandler
from src.internal.app.queries.handlers import Handlers
from src.internal.domain.music.library import Library


def QueryHandlers(local_player) -> List[QueryHandler]:
    """
    Injects application queries, used for getting application state
    :param local_player:
    :return:
    """
    queryHandlers: List[QueryHandler] = []
    queryDeps = {
        "library": Library(),
        "streaming_player": StreamingPlayer(),
        "local_player": local_player
    }

    for h in Handlers:
        queryHandlers.append(h(**queryDeps))

    return queryHandlers
