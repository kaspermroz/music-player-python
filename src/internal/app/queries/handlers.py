from typing import List, Type

from src.internal.app.interfaces.query_handler import QueryHandler
from src.internal.app.queries.get_songs_in_library import GetSongsInLibraryHandler
from src.internal.app.queries.get_local_playlists import GetLocalPlaylistsHandler
from src.internal.app.queries.search_streaming import SearchStreamingHandler
from src.internal.app.queries.get_skipped_songs import GetSkippedSongsHandler

Handlers: List[Type[QueryHandler]] = [
    GetSongsInLibraryHandler,
    GetLocalPlaylistsHandler,
    SearchStreamingHandler,
    GetSkippedSongsHandler,
]
