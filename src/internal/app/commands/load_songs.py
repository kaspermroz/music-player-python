from src.internal.app.interfaces.command_handler import CommandHandler
from src.internal.domain.music.library import Library
from src.internal.domain.music.song import Song


class LoadSongsHandler(CommandHandler):
    library: Library

    def __init__(self, library: Library, **_kwargs):
        self.library = library

    def HandlerName(self) -> str:
        return "LoadSongs"

    def Handle(self, *songs: Song):
        for s in songs:
            self.library.AddSong(s)
