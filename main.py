"""Main module"""
from src.internal.domain.currency import PLN
from src.internal.domain.payments.manager import PaymentsManager
from src.service.di.inject_application import BuildApplication
from src.service.di.inject_event_handlers import EventHandlers
from src.internal.ports.gui.player import PlayerGUI

app = BuildApplication()
eventHandlers = EventHandlers(app)
pm = PaymentsManager(PLN)
player = PlayerGUI(app, eventHandlers, pm)

player.Run()
