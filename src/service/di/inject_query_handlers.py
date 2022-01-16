from typing import List

from src.internal.adapters.streaming_player import StreamingPlayer
from src.internal.app.interfaces.query_handler import QueryHandler
from src.internal.app.queries.handlers import Handlers
from src.internal.domain.music.library import Library


def QueryHandlers() -> List[QueryHandler]:
    queryHandlers: List[QueryHandler] = []
    queryDeps = {
        "library": Library(),
        "streaming_player": StreamingPlayer()
    }

    for h in Handlers:
        queryHandlers.append(h(**queryDeps))

    return queryHandlers
