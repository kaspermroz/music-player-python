from typing import List

from src.internal.app.interfaces.command_handler import CommandHandler
from src.internal.app.interfaces.configuration import Configuration
from src.internal.app.interfaces.query_handler import QueryHandler


class Application:
    """
    Application implementation - holds application commands, queries and config.
    Core of all business logic and center of dependency graph
    """
    LoadSongs = CommandHandler()
    PlaySong = CommandHandler()
    PlayLocalPlaylist = CommandHandler()
    CreateLocalPlaylist = CommandHandler()
    DeleteSong = CommandHandler()
    DeletePlaylist = CommandHandler()
    StopPlayback = CommandHandler()

    GetSongsInLibrary = QueryHandler()
    GetLocalPlaylists = QueryHandler()
    SearchStreaming = QueryHandler()
    GetSkippedSongs = QueryHandler()

    Config = Configuration()

    def __init__(
            self,
            configuration: Configuration,
            commands: List[CommandHandler],
            queries: List[QueryHandler]
    ) -> None:
        self.Config = configuration

        for h in commands:
            setattr(self, h.HandlerName(), h)

        for q in queries:
            setattr(self, q.QueryName(), q)
