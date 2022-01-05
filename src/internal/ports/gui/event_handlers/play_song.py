from src.internal.ports.gui.event_handler import EventHandler
from src.internal.ports.gui.events import EVENT_PLAY_SONG


class PlaySongHandler(EventHandler):
    def EventName(self) -> str:
        return EVENT_PLAY_SONG

    def Handle(self, song_id: str, loop=False):
        self.App.PlaySong.Handle(song_id, loop)
