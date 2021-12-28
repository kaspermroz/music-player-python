"""Main module"""

from src.service.di.inject_application import BuildApplication
from src.internal.ports.gui.player import PlayerGUI

app = BuildApplication()
player = PlayerGUI(app)

player.Run()
