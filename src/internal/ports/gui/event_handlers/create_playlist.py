from src.internal.ports.gui.event_handler import EventHandler
from src.internal.ports.gui.events import EVENT_CREATE_PLAYLIST


class CreatePlaylistHandler(EventHandler):
    """
    Executes when: Player clicks Create Playlist button and types in playlist name in popup
    Functionality: Creates local playlist in library
    """
    def EventName(self) -> str:
        return EVENT_CREATE_PLAYLIST

    def Handle(self, playlist_name: str, *song_ids: str):
        self.App.CreateLocalPlaylist.Handle(playlist_name, song_ids)
