from abc import ABC

from src.internal.domain.music.song import Song
from src.internal.domain.music.playlist import Playlist


class Player(ABC):
    """
    Player interface, every adapter must implement it
    """
    def PlaySongOnce(self, _ : Song):
        raise NotImplementedError

    def PlaySongInLoop(self, _: Song):
        raise NotImplementedError

    def PlayPlaylistOnce(self, _: Playlist):
        raise NotImplementedError

    def PlayPlaylistInLoop(self, _: Playlist):
        raise NotImplementedError
