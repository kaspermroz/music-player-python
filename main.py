"""Main module"""

from src.service.di.inject_application import BuildApplication
from src.service.di.inject_event_handlers import EventHandlers
from src.internal.ports.gui.player import PlayerGUI

app = BuildApplication()
eventHandlers = EventHandlers(app)
player = PlayerGUI(app, eventHandlers)

player.Run()
