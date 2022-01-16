from src.internal.ports.gui.event_handler import EventHandler
from src.internal.ports.gui.events import EVENT_PLAY_PLAYLIST


class PlayPlaylistHandler(EventHandler):
    """
    Executes when: User clicks Play playlist button
    Functionality: Plays local playlist with optional loop
    """
    def EventName(self) -> str:
        return EVENT_PLAY_PLAYLIST

    def Handle(self, playlist_name: str, loop=False):
        self.App.PlayLocalPlaylist.Handle(playlist_name, loop)
