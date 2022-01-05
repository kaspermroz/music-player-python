from src.internal.app.interfaces.command_handler import CommandHandler
from src.internal.app.interfaces.player import Player
from src.internal.domain.music.library import Library


class PlayLocalPlaylistHandler(CommandHandler):
    library: Library
    player: Player

    def __init__(self, library: Library, local_player: Player):
        self.library = library
        self.player = local_player

    def HandlerName(self) -> str:
        return "PlayLocalPlaylist"

    def Handle(self, playlist_name: str, loop: bool):
        playlist = self.library.LocalPlaylists()[playlist_name]

        if loop:
            self.player.PlayPlaylistInLoop(playlist)
        else:
            self.player.PlayPlaylistOnce(playlist)
