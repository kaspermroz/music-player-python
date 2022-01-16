from src.internal.app.interfaces.command_handler import CommandHandler
from src.internal.app.interfaces.player import Player
from src.internal.domain.music.library import Library


class PlaySongHandler(CommandHandler):
    library: Library
    player: Player

    def __init__(self, library: Library, local_player: Player, streaming_player: Player):
        self.library = library
        self.player = local_player
        self.streaming = streaming_player

    def HandlerName(self) -> str:
        return "PlaySong"

    def Handle(self, song_id: str, loop: bool):
        song = self.library.SongByID(song_id)

        if song.IsLocal():
            if loop:
                self.player.PlaySongInLoop(song)
            else:
                self.player.PlaySongOnce(song)
        else:
            if loop:
                self.streaming.PlaySongInLoop(song)
            else:
                self.streaming.PlaySongOnce(song)
