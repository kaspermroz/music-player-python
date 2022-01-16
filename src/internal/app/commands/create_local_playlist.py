from typing import List

from src.internal.app.interfaces.command_handler import CommandHandler
from src.internal.domain.music.library import Library
from src.internal.domain.music.song import Song
from src.internal.domain.music.playlist import Playlist


class CreateLocalPlaylistHandler(CommandHandler):
    """
    Creates local playlists, takes name and local songs to associate with playlist as arguments
    """
    library: Library

    def __init__(self, library: Library, **_kwargs):
        self.library = library

    def HandlerName(self) -> str:
        return "CreateLocalPlaylist"

    def Handle(self, playlist_name: str, song_ids: List[str]):
        songs: List[Song] = []
        for s in song_ids:
            songs.append(self.library.SongByID(s))

        localPlaylist = Playlist(playlist_name)

        localPlaylist.AddSongs(*songs)

        self.library.AddLocalPlaylist(localPlaylist)
