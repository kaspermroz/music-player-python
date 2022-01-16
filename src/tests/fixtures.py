from src.internal.domain.currency import Currency, PLN
from src.internal.domain.money import Money
from src.internal.domain.music.song import Song


def SomeCurrency() -> Currency:
    return PLN


def SomeMoney() -> Money:
    return Money("21.37", SomeCurrency())


def SomeLocalSong(song_id="local") -> Song:
    return Song(song_id, "test", "test", 2137, SomeMoney(), "C:\\Music\\song.mp3")


def SomeStreamingSong(song_id="streaming") -> Song:
    return Song(song_id, "streaming", "str", 1337, SomeMoney(), "http:track:test")
