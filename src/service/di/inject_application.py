from src.internal.app.app import Application
from src.internal.app.commands.handlers import Handlers
from src.service.di.inject_config import ServiceConfig


def BuildApplication() -> Application:
    config = ServiceConfig()

    return Application(
        configuration=config,
        commands=Handlers
    )
