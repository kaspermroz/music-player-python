from src.internal.adapters.streaming_player import StreamingPlayer
from src.internal.app.interfaces.query_handler import QueryHandler
from src.internal.domain.music.library import Library


class SearchStreamingHandler(QueryHandler):
    """
    Returns search results from Spotify based on search phrase
    """
    library: Library
    streaming: StreamingPlayer

    def __init__(self, library: Library, streaming_player: StreamingPlayer, **_kwargs):
        self.streaming = streaming_player
        self.library = library

    def QueryName(self) -> str:
        return "SearchStreaming"

    def Execute(self, search: str) -> any:
        res = self.streaming.Search(search)
        self.library.SetSearchResults(res)

        return res
