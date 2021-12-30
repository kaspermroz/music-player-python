from src.internal.domain.music.song import SongLength


def test_song_length():
    sl1 = SongLength(40)
    assert sl1.Seconds() == 40
    assert sl1.String() == "00:40"

    sl2 = SongLength(70)
    assert sl2.Seconds() == 70
    assert sl2.String() == "01:10"
