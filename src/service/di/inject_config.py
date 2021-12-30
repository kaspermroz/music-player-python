"""Service configuration"""
from dotenv import load_dotenv

from src.internal.app.interfaces.configuration import Configuration


class ServiceConfig(Configuration):
    def __init__(self):
        load_dotenv()

        self.playerSize = (650, 200)

    def PlayerSize(self):
        return self.playerSize
