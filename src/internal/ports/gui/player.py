from typing import List, Dict
import PySimpleGUI as sg

from src.internal.app.app import Application
from src.internal.ports.gui.event_handler import EventHandler
from src.internal.ports.gui.events import EVENT_BROWSE_FILES


class PlayerGUI:
    handlers: Dict[str, EventHandler]

    def __init__(self, application: Application, event_handlers: List[EventHandler]):
        sg.theme("DarkTeal2")
        layout = [
            [sg.Text("Load songs from disk")],
            [sg.FilesBrowse(
                file_types=(("MP3 files", "*.mp3"),),
                initial_folder=application.Config.InitialMusicDirectory(),
                enable_events=True,
                key=EVENT_BROWSE_FILES
            ),
            ],
        ]

        self.window = sg.Window('Music Player', layout=layout, size=application.Config.PlayerSize())
        self.App = application
        self.handlers = {}

        for e in event_handlers:
            self.handlers[e.EventName()] = e

    def Run(self):
        while True:
            event, values = self.window.read()
            shouldFinish = self.handleEvent(event, values)

            if shouldFinish:
                break

        self.window.close()

    def handleEvent(self, event, values) -> bool:
        if event == sg.WIN_CLOSED:
            return True

        self.handlers[event].Handle(values[event])

        return False
