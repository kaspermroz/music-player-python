from src.internal.app.interfaces.command_handler import CommandHandler
from src.internal.domain.music.library import Library


class DeleteSongHandler(CommandHandler):
    """
    Deletes local song by ID
    """
    library: Library

    def __init__(self, library: Library, **_kwargs):
        self.library = library

    def HandlerName(self) -> str:
        return "DeleteSong"

    def Handle(self, song_id: str):
        self.library.RemoveSong(song_id)
