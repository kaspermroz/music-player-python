"""List of all GUI event handlers"""
from typing import List, Type

from src.internal.ports.gui.event_handler import EventHandler
from src.internal.ports.gui.event_handlers.browse_files import BrowseFilesHandler
from src.internal.ports.gui.event_handlers.play_song import PlaySongHandler
from src.internal.ports.gui.event_handlers.create_playlist import CreatePlaylistHandler
from src.internal.ports.gui.event_handlers.play_playlist import PlayPlaylistHandler
from src.internal.ports.gui.event_handlers.delete_song import DeleteSongHandler
from src.internal.ports.gui.event_handlers.delete_playlist import DeletePlaylistHandler
from src.internal.ports.gui.event_handlers.stop import StopHandler

Handlers: List[Type[EventHandler]] = [
    BrowseFilesHandler,
    PlaySongHandler,
    CreatePlaylistHandler,
    PlayPlaylistHandler,
    DeleteSongHandler,
    DeletePlaylistHandler,
    StopHandler,
]
