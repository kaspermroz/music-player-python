from pygame import mixer

from src.internal.app.interfaces.player import Player
from src.internal.domain.music.playlist import Playlist
from src.internal.domain.music.song import Song


class LocalPlayer(Player):
    """
    LocalPlayer is used for handling local playlists and songs from hard drive.
    """
    def __init__(self):
        mixer.init()

    def PlayPlaylistInLoop(self, _: Playlist):
        for song in Playlist.Songs():
            mixer.music.load(song.Path())
            mixer.music.queue(song.Path(), song.Title(), 0)

        mixer.music.play()

    def PlayPlaylistOnce(self, _: Playlist):
        pass

    def PlaySongInLoop(self, _: Song):
        pass

    def PlaySongOnce(self, song: Song):
        mixer.music.unload()
        mixer.music.load(song.Path())
        mixer.music.play()
