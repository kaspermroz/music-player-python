from src.internal.app.app import Application
from src.service.di.inject_config import ServiceConfig
from src.service.di.inject_command_handlers import CommandHandlers
from src.service.di.inject_query_handlers import QueryHandlers
from src.internal.adapters.local_player import LocalPlayer


def BuildApplication() -> Application:
    """
    Returns application injected with all required dependencies.
    :return:
    """
    config = ServiceConfig()
    localPlayer = LocalPlayer()
    handlers = CommandHandlers(localPlayer)
    queries = QueryHandlers(localPlayer)

    return Application(
        configuration=config,
        commands=handlers,
        queries=queries,
    )
