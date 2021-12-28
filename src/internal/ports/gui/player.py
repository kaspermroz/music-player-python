import PySimpleGUI as sg

from src.internal.app.app import Application


EVENT_HI = "Hi"

KEY_HI = "-HI-"


class PlayerGUI:
    def __init__(self, application: Application):
        layout = [
            [sg.Text("Say hi")],
            [sg.Text(size=(40, 1), key=KEY_HI)],
            [sg.Button('Hi')],
        ]

        self.window = sg.Window('Music Player', layout=layout, size=application.Config.PlayerSize())
        self.App = application

    def Run(self):
        while True:
            event, values = self.window.read()
            shouldFinish = self.handleEvent(event, values)

            if shouldFinish:
                break

        self.window.close()

    def handleEvent(self, event, _) -> bool:
        if event == EVENT_HI:
            self.window[KEY_HI].update(self.App.SayHi.Handle())
        elif event == sg.WIN_CLOSED:
            return True

        return False
