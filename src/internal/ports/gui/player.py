from typing import List, Dict
import PySimpleGUI as sg

from src.internal.app.app import Application
from src.internal.ports.gui.event_handler import EventHandler
from src.internal.ports.gui.events import EVENT_BROWSE_FILES


LIST_BOX_LIBRARY = "-LIBRARY-"


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
            )],
            [sg.Listbox(values=[], key=LIST_BOX_LIBRARY, size=(100, 100))]
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

        self.updateUI()

        return False

    def updateUI(self):
        songsInLibrary = self.App.GetSongsInLibrary.Execute()

        songsTitles = [f"{s.Author()} - {s.Title()}" for s in songsInLibrary.values()]

        self.window[LIST_BOX_LIBRARY].update(values=songsTitles)
