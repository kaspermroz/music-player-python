from src.internal.app.interfaces.player import Player
from src.internal.domain.music.playlist import Playlist
from src.internal.domain.music.song import Song


class LocalPlayer(Player):

    def PlayPlaylistInLoop(self, _: Playlist):
        pass

    def PlayPlaylistOnce(self, _: Playlist):
        pass

    def PlaySongInLoop(self, _: Song):
        pass

    def PlaySongOnce(self, _: Song):
        pass
