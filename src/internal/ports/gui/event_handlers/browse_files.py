from ntpath import basename
from uuid import uuid4

from src.internal.domain.currency import Currency
from src.internal.domain.money import Money
from src.internal.domain.music.song import Song
from src.internal.ports.gui.event_handler import EventHandler
from src.internal.ports.gui.events import EVENT_BROWSE_FILES


class BrowseFilesHandler(EventHandler):
    def EventName(self) -> str:
        return EVENT_BROWSE_FILES

    def Handle(self, paths_string: str):
        paths = paths_string.split(';')
        songs = []
        for p in paths:
            song = Song(
                song_id=str(uuid4()),
                author="unknown",
                title=basename(p),
                length=100,
                cost=Money("21.37", Currency("PLN")),
                path=p
            )
            songs.append(song)

        self.App.LoadSongs.Handle(*songs)
