from typing import List, Type

from src.internal.app.commands.load_songs import LoadSongsHandler
from src.internal.app.commands.play_song import PlaySongHandler
from src.internal.app.commands.create_local_playlist import CreateLocalPlaylistHandler
from src.internal.app.commands.play_local_playlist import PlayLocalPlaylistHandler
from src.internal.app.interfaces.command_handler import CommandHandler


Handlers: List[Type[CommandHandler]] = [
    LoadSongsHandler,
    PlaySongHandler,
    CreateLocalPlaylistHandler,
    PlayLocalPlaylistHandler,
]
