from src.internal.app.app import Application
from src.service.di.inject_config import ServiceConfig
from src.service.di.inject_command_handlers import CommandHandlers
from src.service.di.inject_query_handlers import QueryHandlers


def BuildApplication() -> Application:
    config = ServiceConfig()
    handlers = CommandHandlers()
    queries = QueryHandlers()

    return Application(
        configuration=config,
        commands=handlers,
        queries=queries,
    )
