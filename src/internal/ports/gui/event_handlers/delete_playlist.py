from src.internal.ports.gui.event_handler import EventHandler
from src.internal.ports.gui.events import EVENT_DELETE_PLAYLIST


class DeletePlaylistHandler(EventHandler):
    """
    Executes when: User clicks on Delete playlist button
    Functionality: Deletes local playlist by name from library
    """

    def EventName(self) -> str:
        return EVENT_DELETE_PLAYLIST

    def Handle(self, playlist_name: str):
        self.App.DeletePlaylist.Handle(playlist_name)
