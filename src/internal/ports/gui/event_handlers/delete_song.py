from src.internal.ports.gui.event_handler import EventHandler
from src.internal.ports.gui.events import EVENT_DELETE_SONG


class DeleteSongHandler(EventHandler):
    """
    Executes when: Player clicks Delete song button
    Functionality: Deletes local song object from library
    """
    def EventName(self) -> str:
        return EVENT_DELETE_SONG

    def Handle(self, song_id):
        self.App.DeleteSong.Handle(song_id)
