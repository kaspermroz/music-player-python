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
        pass

    def PlayPlaylistOnce(self, playlist: Playlist):
        mixer.music.unload()
        songs = playlist.Songs()

        mixer.music.load(songs[0].Path())

        for song in songs[1:]:
            mixer.music.queue(song.Path(), song.Title(), 0)

        mixer.music.play()

    def PlaySongInLoop(self, _: Song):
        pass

    def PlaySongOnce(self, song: Song):
        mixer.music.unload()
        mixer.music.load(song.Path())
        mixer.music.play()
