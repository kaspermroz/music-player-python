from src.internal.app.interfaces.command_handler import CommandHandler
from src.internal.app.interfaces.player import Player


class StopPlaybackHandler(CommandHandler):
    """
    Stops all playback
    """
    player: Player

    def __init__(self, local_player: Player, **_kwargs):
        self.player = local_player

    def HandlerName(self) -> str:
        return "StopPlayback"

    def Handle(self):
        self.player.Stop()
