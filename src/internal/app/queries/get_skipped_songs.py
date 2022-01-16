from src.internal.adapters.local_player import LocalPlayer
from src.internal.app.interfaces.query_handler import QueryHandler


class GetSkippedSongsHandler(QueryHandler):
    player: LocalPlayer

    def __init__(self, local_player: LocalPlayer, **_kwargs):
        self.player = local_player

    def QueryName(self) -> str:
        return "GetSkippedSongs"

    def Execute(self) -> any:
        return self.player.SkippedSongs()
