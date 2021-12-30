from typing import Dict

from src.internal.domain.music.song import Song
from src.internal.domain.music.playlist import Playlist
from src.service.singleton import Singleton


class Library(metaclass=Singleton):
    """
    Library is used for storing songs available to be added to playlist or played individually.
    User is limited to one library with multiple playlists.
    """

    songs: Dict[str, Song]
    localPlaylists: Dict[str, Playlist]
    streamingPlaylists: Dict[str, Playlist]

    def __init__(self):
        self.songs = {}
        self.localPlaylists = {}
        self.streamingPlaylists = {}

    def Songs(self) -> Dict[str, Song]:
        return self.songs

    def LocalPlaylists(self) -> Dict[str, Playlist]:
        return self.localPlaylists

    def StreamingPlaylists(self) -> Dict[str, Playlist]:
        return self.streamingPlaylists

    def AddSong(self, song: Song):
        self.songs[song.ID()] = song

    def RemoveSong(self, song: Song):
        if song.ID() in self.songs:
            del self.songs[song.ID()]
