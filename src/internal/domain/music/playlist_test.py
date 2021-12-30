from pytest import raises

from src.internal.domain.music.playlist import Playlist, PlaylistTypeError
from src.tests.fixtures import SomeLocalSong, SomeStreamingSong


def test_local_playlist():
    p = Playlist("local")
    ls = SomeLocalSong()

    p.AddSongs(ls)

    assert len(p.Songs()) == 1
    assert p.Songs()[0].ID() == ls.ID()

    with raises(PlaylistTypeError) as pte:
        ss = SomeStreamingSong()
        p.AddSongs(ss)

    assert pte.value.message == "song does not match local playlist type"


def test_streaming_playlist():
    p = Playlist("streaming", False)
    ss = SomeStreamingSong()

    p.AddSongs(ss)

    assert len(p.Songs()) == 1
    assert p.Songs()[0].ID() == ss.ID()

    with raises(PlaylistTypeError) as pte:
        ls = SomeLocalSong()
        p.AddSongs(ls)

    assert pte.value.message == "song does not match non-local playlist type"
