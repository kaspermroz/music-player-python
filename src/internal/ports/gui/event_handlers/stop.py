from src.internal.ports.gui.event_handler import EventHandler
from src.internal.ports.gui.events import EVENT_STOP


class StopHandler(EventHandler):
    """
       Executes when: User clicks STOP button
       Functionality: Stops all playback
    """
    def EventName(self) -> str:
        return EVENT_STOP

    def Handle(self):
        self.App.StopPlayback.Handle()
