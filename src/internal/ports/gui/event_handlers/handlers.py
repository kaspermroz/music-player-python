from typing import List, Type

from src.internal.ports.gui.event_handler import EventHandler
from src.internal.ports.gui.event_handlers.browse_files import BrowseFilesHandler

Handlers: List[Type[EventHandler]] = [
    BrowseFilesHandler,
]
