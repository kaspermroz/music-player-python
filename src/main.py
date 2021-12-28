"""Main module"""

from internal.app.app import Application
from internal.app.commands.handlers import Handlers

app = Application(Handlers)

app.SayHi.Handle()
