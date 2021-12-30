from src.internal.domain.music.library import Library
from src.tests.fixtures import SomeLocalSong


def test_library_is_singleton():
    lib = Library()
    s = SomeLocalSong("local")
    lib.AddSong(s)

    assert len(lib.Songs()) == 1
    assert s.ID() in lib.Songs()

    lib2 = Library()

    assert len(lib2.Songs()) == 1
    assert s.ID() in lib2.Songs()
