from src.internal.domain.currency import Currency, PLN
from src.internal.domain.money import Money
from src.internal.domain.music.song import Song


def SomeCurrency() -> Currency:
    """Returns PLN Currency"""
    return PLN


def SomeMoney() -> Money:
    """Returns Money instance """
    return Money("21.37", SomeCurrency())


def SomeLocalSong(song_id="local") -> Song:
    """Returns sample local song instance"""
    return Song(song_id, "test", "test", 2137, SomeMoney(), "C:\\Music\\song.mp3")


def SomeStreamingSong(song_id="streaming") -> Song:
    """Returns sample streaming song instance"""
    return Song(song_id, "streaming", "str", 1337, SomeMoney(), "http:track:test")
