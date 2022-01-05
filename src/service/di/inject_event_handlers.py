from typing import List

from src.internal.app.app import Application
from src.internal.ports.gui.event_handler import EventHandler
from src.internal.ports.gui.event_handlers.handlers import Handlers


def EventHandlers(app: Application) -> List[EventHandler]:
    eventHandlers: List[EventHandler] = []
    eventDeps = {
        "application": app
    }

    for h in Handlers:
        handler = h(**eventDeps)
        eventHandlers.append(handler)

    return eventHandlers
