from uuid import uuid4
from random import triangular
from webbrowser import open as wopen
from spotipy import SpotifyClientCredentials, Spotify


from src.internal.app.interfaces.player import Player
from src.internal.domain.music.song import Song
from src.internal.domain.music.playlist import Playlist
from src.internal.domain.money import Money
from src.internal.domain.currency import PLN


class StreamingPlayer(Player):
    def __init__(self):
        self.spotify = Spotify(client_credentials_manager=SpotifyClientCredentials())

    def PlaySongOnce(self, s: Song):
        wopen(s.Path())

    def PlaySongInLoop(self, _: Song):
        raise NotImplementedError

    def PlayPlaylistOnce(self, _: Playlist):
        raise NotImplementedError

    def PlayPlaylistInLoop(self, _: Playlist):
        raise NotImplementedError

    def Search(self, search: str):
        res = self.spotify.search(q=search)["tracks"]["items"][0:5]

        return [
            Song(
                song_id=str(uuid4()),
                author=", ".join([a["name"] for a in i["artists"]]),
                title=i["name"],
                length=round(i["duration_ms"] / 1000),
                cost=getCostByYear(2020),
                path=i["preview_url"]
            ) for i in res]


def getCostByYear(year: int) -> Money:
    value = round(triangular(0.20, 4.00, year / 2022 * 3), 2)

    return Money(str(value), PLN)
