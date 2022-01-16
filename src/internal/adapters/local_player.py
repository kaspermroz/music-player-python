from typing import List
from threading import Thread
from time import sleep
from pygame import mixer, time

from src.internal.app.interfaces.player import Player
from src.internal.domain.music.playlist import Playlist
from src.internal.domain.music.song import Song


CONTINUOUS_LOOP = 1000000


class LocalPlayer(Player):
    shouldStop: bool
    skippedSongs: List[Song]
    """
    LocalPlayer is used for handling local playlists and songs from hard drive.
    """
    def __init__(self):
        self.shouldStop = False
        self.skippedSongs = []
        mixer.init()

    def PlayPlaylistInLoop(self, playlist: Playlist):
        self.PlayPlaylistOnce(playlist, CONTINUOUS_LOOP)

    def PlayPlaylistOnce(self, playlist: Playlist, loops=1):
        self.skippedSongs = playlist.Songs()[1:]

        def play():
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

        def countCost():
            for s in playlist.Songs():
                sleep(s.Length().Seconds())
                if len(self.skippedSongs) > 0:
                    self.skippedSongs = self.skippedSongs[1:]

        Thread(target=play).start()
        Thread(target=countCost).start()

    def PlaySongInLoop(self, song: Song):
        self.PlaySongOnce(song, CONTINUOUS_LOOP)

    def PlaySongOnce(self, song: Song, loops=0):
        mixer.music.unload()
        mixer.music.load(song.Path())
        mixer.music.play(loops=loops)

    def Stop(self):
        self.shouldStop = True
        time.wait(500)
        mixer.music.stop()

    def SkippedSongs(self) -> List[Song]:
        return self.skippedSongs
