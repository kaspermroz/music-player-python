from src.internal.app.interfaces.command_handler import CommandHandler
from src.internal.domain.music.library import Library


class DeletePlaylistHandler(CommandHandler):
    library: Library

    def __init__(self, library: Library, **_kwargs):
        self.library = library

    def HandlerName(self) -> str:
        return "DeletePlaylist"

    def Handle(self, song_id: str):
        self.library.RemoveLocalPlaylist(song_id)
