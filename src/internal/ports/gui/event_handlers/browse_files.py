from random import triangular
from ntpath import basename
from uuid import uuid4
from mutagen.mp3 import MP3

from src.internal.domain.currency import PLN
from src.internal.domain.money import Money
from src.internal.domain.music.song import Song
from src.internal.ports.gui.event_handler import EventHandler
from src.internal.ports.gui.events import EVENT_BROWSE_FILES


AUTHOR_TAG = "TIT2"
TITLE_TAG = "TPE1"
YEAR_TAG = "TDRC"


class BrowseFilesHandler(EventHandler):
    """
    Executes when: User selects MP3 files from disc
    Functionality: Loads mp3 files and creates Song objects,
    puts songs in library
    """
    def EventName(self) -> str:
        return EVENT_BROWSE_FILES

    def Handle(self, paths_string: str):
        paths = paths_string.split(';')
        songs = []
        for p in paths:
            author = "unknown"
            title = basename(p).split('.')[0]
            audio = MP3(p)
            year = 2000

            if AUTHOR_TAG in audio.tags:
                author = audio.tags[AUTHOR_TAG]
            if TITLE_TAG in audio.tags:
                title = audio.tags[TITLE_TAG]
            if YEAR_TAG in audio.tags:
                print(audio.tags[YEAR_TAG])
                year = int(audio.tags[YEAR_TAG].text[0].text)

            song = Song(
                song_id=str(uuid4()),
                author=author,
                title=title,
                length=audio.info.length,
                cost=getCostByYear(year),
                path=p
            )
            songs.append(song)

        self.App.LoadSongs.Handle(*songs)


def getCostByYear(year: int) -> Money:
    value = round(triangular(0.20, 4.00, year/2022 * 3), 2)

    return Money(str(value), PLN)
