from typing import List, Type

from src.internal.app.interfaces.query_handler import QueryHandler
from src.internal.app.queries.get_songs_in_library import GetSongsInLibraryHandler
from src.internal.app.queries.get_local_playlists import GetLocalPlaylistsHandler

Handlers: List[Type[QueryHandler]] = [
    GetSongsInLibraryHandler,
    GetLocalPlaylistsHandler,
]
