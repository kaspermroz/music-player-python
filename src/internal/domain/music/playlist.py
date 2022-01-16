from typing import List

from src.internal.domain.music.song import Song
from src.internal.domain.money import Money
from src.internal.domain.currency import PLN


class PlaylistTypeError(Exception):
    """
    Exception raised when local song is added to non-local playlist and the other way around
    """

    message: str

    def __init__(self, is_local: bool):
        playlistType = "non-local"

        if is_local:
            playlistType = "local"

        msg = f"song does not match {playlistType} playlist type"

        self.message = msg
        super().__init__(self.message)


class Playlist:
    """
    Domain object for playlists, holds name, isLocal flag and list of songs
    """
    name: str
    isLocal: bool
    songs: List[Song]

    def __init__(self, name: str, is_local=True):
        self.name = name
        self.isLocal = is_local
        self.songs = []

    def Name(self) -> str:
        return self.name

    def IsLocal(self) -> bool:
        return self.isLocal

    def Songs(self) -> List[Song]:
        return self.songs

    def AddSongs(self, *songs: Song):
        for s in songs:
            if s.IsLocal() is not self.isLocal:
                raise PlaylistTypeError(self.isLocal)
            self.songs.append(s)

    def RemoveSong(self, song: Song):
        self.songs = [s for s in self.songs if s.ID() is not song.ID()]

    def GetTotalCost(self) -> Money:
        cost = Money("0.00", PLN)

        for s in self.songs:
            cost += s.Cost()

        return cost
