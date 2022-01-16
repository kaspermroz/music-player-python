from abc import ABC

from src.internal.app.app import Application


class EventHandler(ABC):
    """
    Event Handler interface for PySimpleGUI events.
    Used for implementation of classes executed as a response to all user actions
    """

    App: Application

    def __init__(self, application: Application, *_args, **_kwargs):
        self.App = application

    def EventName(self) -> str:
        raise NotImplementedError

    def Handle(self, *values: any):
        raise NotImplementedError
