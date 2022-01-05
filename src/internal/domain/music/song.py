from time import strftime, gmtime

from src.internal.domain.money import Money


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
    """
    Song is a class added for simplicity of handling both
    local and streaming songs added to library. Players are responsible
    for handling specific song playing based on path and costs.
    """
    id: str
    author: str
    title: str
    length: SongLength
    cost: Money
    path: str

    def __init__(self, song_id: str, author: str, title: str, length: int, cost: Money, path: str):
        self.id = song_id
        self.author = author
        self.title = title
        self.length = SongLength(length)
        self.cost = cost
        self.path = path

    def ID(self) -> str:
        return self.id

    def Author(self) -> str:
        return self.author

    def Title(self) -> str:
        return self.title

    def Length(self) -> SongLength:
        return self.length

    def Path(self) -> str:
        return self.path

    def IsLocal(self) -> bool:
        return not self.path.startswith("spotify")
