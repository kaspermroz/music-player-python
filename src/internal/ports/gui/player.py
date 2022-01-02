from typing import List, Dict
import PySimpleGUI as sg

from src.internal.app.app import Application
from src.internal.ports.gui.event_handler import EventHandler
from src.internal.ports.gui.events import EVENT_PLAY_SONG, \
    EVENT_SELECT_SINGLE_SONG, \
    EVENT_BROWSE_FILES



class PlayerGUI:
    handlers: Dict[str, EventHandler]

    def __init__(self, application: Application, event_handlers: List[EventHandler]):
        sg.theme("DarkTeal2")
        layout = [
            [sg.Text("Load songs from disk")],
            [sg.Button(button_text="Play Song", key=EVENT_PLAY_SONG)],
            [sg.FilesBrowse(
                file_types=(("MP3 files", "*.mp3"),),
                initial_folder=application.Config.InitialMusicDirectory(),
                enable_events=True,
                key=EVENT_BROWSE_FILES
            )],
            [sg.Listbox(
                values=[],
                key=EVENT_SELECT_SINGLE_SONG,
                size=(50, 10), enable_events=True)],
        ]

        self.window = sg.Window('Music Player', layout=layout, size=application.Config.PlayerSize())
        self.App = application
        self.handlers = {}
        self.songIds = {}
        self.selectedSong = None

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
        elif event == EVENT_BROWSE_FILES:
            self.handlers[event].Handle(values[event])
        elif event == EVENT_PLAY_SONG:
            if self.selectedSong is None:
                return False

            songId = self.songIds[self.selectedSong]
            self.handlers[event].Handle(songId)
        elif event == EVENT_SELECT_SINGLE_SONG:
            print(values[event])
            self.selectedSong = values[event][0]

        self.updateUI()

        return False

    def updateUI(self):
        songsInLibrary = self.App.GetSongsInLibrary.Execute()
        songTitles = []

        for songID, song in songsInLibrary.items():
            songSlug = f"{song.Author()} - {song.Title()}"
            songTitles.append(songSlug)
            self.songIds[songSlug] = songID

        self.window[EVENT_SELECT_SINGLE_SONG].update(values=songTitles)
