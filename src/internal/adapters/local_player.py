from threading import Thread
from pygame import mixer, time

from src.internal.app.interfaces.player import Player
from src.internal.domain.music.playlist import Playlist
from src.internal.domain.music.song import Song


CONTINUOUS_LOOP = 1000000


class LocalPlayer(Player):
    shouldStop: bool
    """
    LocalPlayer is used for handling local playlists and songs from hard drive.
    """
    def __init__(self):
        self.shouldStop = False
        mixer.init()

    def PlayPlaylistInLoop(self, playlist: Playlist):
        self.PlayPlaylistOnce(playlist, CONTINUOUS_LOOP)

    def PlayPlaylistOnce(self, playlist: Playlist, loops=1):
        def worker():
            for _ in range(loops):
                mixer.music.unload()
                songs = playlist.Songs()

                mixer.music.load(songs[0].Path())

                for song in songs[1:]:
                    mixer.music.queue(song.Path())

                mixer.music.play()

                while mixer.music.get_busy():
                    if self.shouldStop:
                        mixer.music.stop()
                        self.shouldStop = False
                        return
                    time.wait(200)

        Thread(target=worker).start()

    def PlaySongInLoop(self, song: Song):
        self.PlaySongOnce(song, CONTINUOUS_LOOP)

    def PlaySongOnce(self, song: Song, loops=0):
        mixer.music.unload()
        mixer.music.load(song.Path())
        mixer.music.play(loops=loops)

    def Stop(self):
        mixer.music.stop()
        self.shouldStop = True
