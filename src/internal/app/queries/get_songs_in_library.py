from src.internal.app.interfaces.query_handler import QueryHandler
from src.internal.domain.music.library import Library


class GetSongsInLibraryHandler(QueryHandler):
    """
    Returns all songs from library
    """
    library: Library

    def __init__(self, library: Library, **_kwargs):
        self.library = library

    def QueryName(self) -> str:
        return "GetSongsInLibrary"

    def Execute(self, *_args, **_kwargs) -> any:
        return self.library.Songs()
