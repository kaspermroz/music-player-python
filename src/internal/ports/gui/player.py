from typing import List, Dict
import PySimpleGUI as sg

from src.internal.app.app import Application
from src.internal.ports.gui.event_handler import EventHandler
from src.internal.ports.gui.events import EVENT_PLAY_SONG, \
    EVENT_SELECT_SONGS, \
    EVENT_BROWSE_FILES, \
    EVENT_CREATE_PLAYLIST, \
    EVENT_SELECT_PLAYLIST, \
    EVENT_PLAY_PLAYLIST


class PlayerGUI:
    handlers: Dict[str, EventHandler]

    def __init__(self, application: Application, event_handlers: List[EventHandler]):
        sg.theme("DarkTeal2")
        layout = [
            [sg.Button(button_text="Play Song", key=EVENT_PLAY_SONG)],
            [sg.Button(button_text="Create Playlist",  key=EVENT_CREATE_PLAYLIST)],
            [sg.Button(button_text="Play Playlist",  key=EVENT_PLAY_PLAYLIST)],
            [sg.FilesBrowse(
                button_text="Load MP3 files from disk",
                file_types=(("MP3 files", "*.mp3"),),
                initial_folder=application.Config.InitialMusicDirectory(),
                enable_events=True,
                key=EVENT_BROWSE_FILES
            )],
            [sg.Text("Library")],
            [sg.Listbox(
                values=[],
                select_mode=sg.SELECT_MODE_MULTIPLE,
                key=EVENT_SELECT_SONGS,
                size=(100, 10), enable_events=True)],
            [sg.Text("Local Playlists")],
            [sg.Listbox(
                values=[],
                key=EVENT_SELECT_PLAYLIST,
                size=(100, 10), enable_events=True)],
        ]

        self.window = sg.Window('Music Player', layout=layout, size=application.Config.PlayerSize())
        self.App = application
        self.handlers = {}
        self.songIds = {}
        self.selectedSongs = []
        self.selectedPlaylist = None

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

        elif event == EVENT_PLAY_SONG:
            if self.selectedSongs is None:
                return False

            songId = self.songIds[self.selectedSongs[0]]
            self.handlers[event].Handle(songId)
        elif event == EVENT_SELECT_SONGS:
            if len(values[event]) > 0:
                self.selectedSongs = values[event]

        elif event == EVENT_CREATE_PLAYLIST:
            if self.selectedSongs is None:
                return False

            name = sg.popup_get_text(
                title="Create playlist",
                message="Enter playlist name",
                default_text="my_playlist",
            )

            if name is None:
                return False

            songIds = []
            for s in self.selectedSongs:
                songIds.append(self.songIds[s])
            self.handlers[event].Handle(name, *songIds)
            self.updateLocalPlaylists()

        elif event == EVENT_SELECT_PLAYLIST:
            self.selectedPlaylist = values[event][0]

        elif event == EVENT_PLAY_PLAYLIST:
            self.handlers[event].Handle(self.selectedPlaylist)

        else:
            self.handlers[event].Handle(values[event])
            self.updateLibrary()

        return False

    def updateLibrary(self):
        songsInLibrary = self.App.GetSongsInLibrary.Execute()
        songTitles = []

        for songID, song in songsInLibrary.items():
            songSlug = f"{song.Author()} - {song.Title()}"
            songTitles.append(songSlug)
            self.songIds[songSlug] = songID

        self.window[EVENT_SELECT_SONGS].update(values=songTitles)

    def updateLocalPlaylists(self):
        localPlaylists = self.App.GetLocalPlaylists.Execute()
        playlistNames = []
        for name in localPlaylists.keys():
            playlistNames.append(name)

        self.window[EVENT_SELECT_PLAYLIST].update(values=playlistNames)
