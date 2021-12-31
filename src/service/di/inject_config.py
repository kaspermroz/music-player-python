"""Service configuration"""
from os import getenv
from typing import Tuple
from dotenv import load_dotenv

from src.internal.app.interfaces.configuration import Configuration


class ServiceConfig(Configuration):
    def __init__(self):
        load_dotenv()

        self.playerSize = (650, 200)
        self.initialMusicDir = getenv('INITIAL_MUSIC_DIRECTORY')

    def PlayerSize(self) -> Tuple[int, int]:
        return self.playerSize

    def InitialMusicDirectory(self) -> str:
        return self.initialMusicDir
