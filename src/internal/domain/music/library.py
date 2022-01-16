from typing import Dict, List

from src.internal.domain.music.song import Song
from src.internal.domain.music.playlist import Playlist
from src.service.singleton import Singleton


class Library(metaclass=Singleton):
    """
    Library is used for storing songs available to be added to playlist or played individually.
    User is limited to one library with multiple playlists.
    Uses singleton as metaclass to ensure deduplication and coherence of state.
    """

    songs: Dict[str, Song]
    searchResults: Dict[str, Song]
    localPlaylists: Dict[str, Playlist]
    streamingPlaylists: Dict[str, Playlist]

    def __init__(self):
        self.songs = {}
        self.searchResults = {}
        self.localPlaylists = {}
        self.streamingPlaylists = {}

    def Songs(self) -> Dict[str, Song]:
        return self.songs

    def SongByID(self, song_id: str) -> Song:
        if song_id in self.songs.keys():
            return self.songs[song_id]

        return self.searchResults[song_id]

    def LocalPlaylists(self) -> Dict[str, Playlist]:
        return self.localPlaylists

    def StreamingPlaylists(self) -> Dict[str, Playlist]:
        return self.streamingPlaylists

    def AddSong(self, song: Song):
        self.songs[song.ID()] = song

    def SetSearchResults(self, songs: List[Song]):
        self.searchResults = {s.ID(): s for s in songs}

    def RemoveSong(self, song_id: str):
        if song_id in self.songs:
            del self.songs[song_id]

        print(self.songs)

    def AddLocalPlaylist(self, local_playlist: Playlist):
        self.localPlaylists[local_playlist.Name()] = local_playlist

    def RemoveLocalPlaylist(self, playlist_name: str):
        if playlist_name in self.localPlaylists.keys():
            del self.localPlaylists[playlist_name]
