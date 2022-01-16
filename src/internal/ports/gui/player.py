from typing import List, Dict
from decimal import Decimal
import PySimpleGUI as sg

from src.internal.app.app import Application
from src.internal.domain.payments.coin import *
from src.internal.domain.payments.manager import PaymentsManager
from src.internal.domain.money import Money
from src.internal.ports.gui.event_handler import EventHandler
from src.internal.ports.gui.events import *


LOOP = "-LOOP-"
CREDIT = "-CREDIT-"
PAID = "-PAID-"
SWITCH = "-SWITCH-"
"""GUI elements without dedicated events"""

coinsMap = {
    "0.10": Coin10GR,
    "0.20": Coin20GR,
    "0.50": Coin50GR,
    "1.00": Coin1PLN,
    "1": Coin1PLN,
    "2.00": Coin2PLN,
    "2": Coin2PLN,
    "5.00": Coin5PLN,
    "5": Coin5PLN,
}
"""Map of user input to coins"""


class PlayerGUI:
    """
    Implementation of GUI port, uses PySimpleGUI library for building layout.
    Has Application as dependency in order to use commands and queries.
    Has PaymentsManager as dependency for payments functionality.
    """
    handlers: Dict[str, EventHandler]

    def __init__(self, application: Application, event_handlers: List[EventHandler],
                 payments_manager: PaymentsManager):
        self.App = application
        self.handlers = {}
        self.songIds = {}
        self.selectedSongs = []
        self.selectedPlaylist = None
        self.pm = payments_manager
        self.isLocalMode = True
        self.searchResults = {}

        sg.theme("DarkTeal2")
        layout = [
            [sg.Button(button_text="Switch Mode", key=SWITCH), sg.Checkbox(text="Loop", key=LOOP)],
            [
                sg.Text("Credit: "),
                sg.Text(str(self.pm.Credit()), key=CREDIT),
                sg.Text("Paid: "),
                sg.Text(str(self.pm.SumIn()), key=PAID),
                sg.Button(button_text="Insert Coin", key=EVENT_INSERT_COIN),
                sg.Button(button_text="Get Change", key=EVENT_GET_CHANGE),
            ],
            [
                sg.FilesBrowse(
                    button_text="Load MP3 files from disk",
                    file_types=(("MP3 files", "*.mp3"),),
                    initial_folder=application.Config.InitialMusicDirectory(),
                    enable_events=True,
                    key=EVENT_BROWSE_FILES),
            ],
            [sg.Input(
                    default_text="Search Spotify...",
                    enable_events=True,
                    key=EVENT_SEARCH_STREAMING,
                    visible=False
                )],
            [
                sg.Button(button_text="Play Song", key=EVENT_PLAY_SONG),
                sg.Button(button_text="Delete Song", key=EVENT_DELETE_SONG),
                sg.Button(button_text="STOP", key=EVENT_STOP)
            ],

            [sg.Text("Library")],
            [sg.Listbox(
                values=[],
                select_mode=sg.SELECT_MODE_MULTIPLE,
                key=EVENT_SELECT_SONGS,
                size=(100, 10), enable_events=True)],
            [
                sg.Button(button_text="Create Playlist", key=EVENT_CREATE_PLAYLIST),
                sg.Button(button_text="Play Playlist", key=EVENT_PLAY_PLAYLIST),
                sg.Button(button_text="Delete Playlist", key=EVENT_DELETE_PLAYLIST),
            ],
            [sg.Text("Playlists")],
            [sg.Listbox(
                values=[],
                key=EVENT_SELECT_PLAYLIST,
                size=(100, 10), enable_events=True)],
        ]

        self.window = sg.Window('Music Player', layout=layout, size=application.Config.PlayerSize())

        for e in event_handlers:
            self.handlers[e.EventName()] = e

    def Run(self):
        """
        Method for opening GUI and listening to user events.
        :return:
        """
        while True:
            event, values = self.window.read()
            shouldFinish = self.handleEvent(event, values)

            if shouldFinish:
                break

        self.window.close()

    def switchMode(self):
        """
        Used for switching between local and streaming mode
        :return:
        """
        self.isLocalMode = not self.isLocalMode
        self.window[EVENT_BROWSE_FILES].update(visible=self.isLocalMode)
        self.window[EVENT_SEARCH_STREAMING].update(visible=not self.isLocalMode)

        if self.isLocalMode:
            self.updateLibrary()
            self.updateLocalPlaylists()

        else:
            self.window[EVENT_SELECT_SONGS].update(values=[])
            self.window[EVENT_SELECT_PLAYLIST].update(values=[])

    def handleEvent(self, event, values) -> bool:
        """
        Method for handling GUI events inside a loop (clicks, inputs, etc).
        Returns boolean with meanings:
        False - do not finish, continue to listen to events
        True - end program execution

        :param event:
        :param values:
        :return:
        """

        if event == sg.WIN_CLOSED:
            return True

        if event == EVENT_STOP:
            self.handlers[event].Handle()
            refund = self.pm.moneyZero()
            skipped = self.App.GetSkippedSongs.Execute()

            for s in skipped:
                refund += getRefundCost(s.Cost())

            self.pm.AddMoney(refund)
            self.updateMoney()

        elif event == EVENT_PLAY_SONG:
            if len(self.selectedSongs) == 0:
                return False

            songId = self.songIds[self.selectedSongs[0]]
            cost = self.getSongCostByID(songId)
            if self.isLocalMode:
                cost = getLocalCost(cost)
            if values[LOOP]:
                cost = getLoopCost(cost)

            self.pm.AddCredit(cost)

            self.updateMoney()
            self.handlers[event].Handle(songId, values[LOOP])

        elif event == EVENT_DELETE_SONG:
            if len(self.selectedSongs) == 0 or not self.isLocalMode:
                return False

            songId = self.songIds[self.selectedSongs[0]]

            self.handlers[event].Handle(songId)
            self.updateLibrary()

        elif event == EVENT_SELECT_SONGS:
            if len(values[event]) > 0:
                self.selectedSongs = values[event]

        elif event == EVENT_CREATE_PLAYLIST:
            if len(self.selectedSongs) == 0:
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
            if self.selectedPlaylist is None:
                return False

            cost = self.getPlaylistCostByName(self.selectedPlaylist)
            if self.isLocalMode:
                cost = getLocalCost(cost)
            if values[LOOP]:
                cost = getLoopCost(cost)

            self.pm.AddCredit(cost)
            self.updateMoney()

            self.handlers[event].Handle(self.selectedPlaylist, values[LOOP])

        elif event == EVENT_DELETE_PLAYLIST:
            if self.selectedPlaylist is None:
                return False

            self.handlers[event].Handle(self.selectedPlaylist)
            self.updateLocalPlaylists()

        elif event == EVENT_INSERT_COIN:
            value = sg.popup_get_text(message="Coin value")

            if value not in coinsMap.keys():
                sg.Popup("Invalid Amount")

            else:
                self.pm.AddCoin(coinsMap[value])
                self.updateMoney()

        elif event == EVENT_GET_CHANGE:
            if self.pm.SumIn().IsZero():
                sg.Popup("No cash to get")
            else:
                change = self.pm.GetChange(self.pm.Credit())
                sg.Popup(", ".join([str(c.Value()) for c in change]))
                self.updateMoney()

        elif event == SWITCH:
            self.switchMode()

        elif event == EVENT_SEARCH_STREAMING:
            search = values[EVENT_SEARCH_STREAMING]
            if len(search) > 2:
                results = self.App.SearchStreaming.Execute(search)
                songTitles = []

                for song in results:
                    songSlug = f"{song.Author()} - {song.Title()} ({song.Cost()})"
                    songTitles.append(songSlug)
                    self.songIds[songSlug] = song.ID()
                    self.searchResults[song.ID()] = song

                self.window[EVENT_SELECT_SONGS].update(values=songTitles)

        else:
            self.handlers[event].Handle(values[event])
            self.updateLibrary()

        return False

    def updateLibrary(self):
        """
        Updates GUI library with local songs
        :return:
        """
        songsInLibrary = self.App.GetSongsInLibrary.Execute()
        songTitles = []

        for songID, song in songsInLibrary.items():
            songSlug = f"{song.Author()} - {song.Title()} ({song.Cost()})"
            songTitles.append(songSlug)
            self.songIds[songSlug] = songID

        self.window[EVENT_SELECT_SONGS].update(values=songTitles)

    def updateLocalPlaylists(self):
        """
        Updates GUI with local playlists
        :return:
        """
        localPlaylists = self.App.GetLocalPlaylists.Execute()
        playlistNames = []
        for name in localPlaylists.keys():
            playlistNames.append(name)

        self.window[EVENT_SELECT_PLAYLIST].update(values=playlistNames)

    def updateMoney(self):
        """
        Updates Paid and Credit information using PaymentsManager
        :return:
        """
        self.window[CREDIT].update(value=str(self.pm.Credit()))
        self.window[PAID].update(value=str(self.pm.SumIn()))

    def getSongCostByID(self, song_id: str) -> Money:
        """
        Returns cost of song by ID
        :param song_id:
        :return:
        """
        if self.isLocalMode:
            return self.App.GetSongsInLibrary.Execute()[song_id].Cost()
        else:
            return self.searchResults[song_id].Cost()

    def getPlaylistCostByName(self, playlist: str) -> Money:
        """
        Returns accumulated cost of playlist by name
        :param playlist:
        :return:
        """
        return self.App.GetLocalPlaylists.Execute()[playlist].GetTotalCost()

getLocalCost = lambda cost: Money(str(round(cost.Amount()/2, 2)), cost.Currency())
"""Cuts the price of local songs by half"""

getLoopCost = lambda cost: Money(str(round(cost.Amount()*Decimal(1.25), 2)), cost.Currency())
"""Adds 25% of song value when in loop"""

getRefundCost = lambda cost: Money(str(round(cost.Amount()*Decimal(0.45), 2)), cost.Currency())
"""Calculates refunds of local songs (10% of half-base cost - 5% refund)"""
