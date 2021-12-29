from time import strftime, gmtime


class SongLength:
    """
    SongLength is a class for easier length handling, both in seconds and human-readable format
    """
    seconds: int

    def __init__(self, seconds: int):
        self.seconds = seconds

    def Seconds(self) -> int:
        return self.seconds

    def String(self) -> str:
        return strftime("%M:%S", gmtime(self.seconds))


class Song:
    id: str
    author: str
    title: str
    length: SongLength

    def __init__(self, song_id: str, author: str, title: str, length: int):
        self.id = song_id
        self.author = author
        self.title = title
        self.length = SongLength(length)

    def ID(self) -> str:
        return self.id

    def Author(self) -> str:
        return self.author

    def Length(self) -> SongLength:
        return self.length
