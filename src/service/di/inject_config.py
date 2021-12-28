"""Service configuration"""

from src.internal.app.interfaces.configuration import Configuration


class ServiceConfig(Configuration):
    def __init__(self):
        self.playerSize = (650, 200)

    def PlayerSize(self):
        return self.playerSize
