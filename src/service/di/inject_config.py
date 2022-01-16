"""Service configuration"""
from os import getenv, add_dll_directory, getcwd
from typing import Tuple
from dotenv import load_dotenv

from src.internal.app.interfaces.configuration import Configuration


class ServiceConfig(Configuration):
    """
    Implementation of Configuration interface, loads env vars from .env file and DLL for pygame module
    """
    def __init__(self):
        add_dll_directory(f"{getcwd()}\\venv\\Lib\\site-packages\\pygame")
        load_dotenv()

        self.playerSize = (800, 600)
        self.initialMusicDir = getenv('INITIAL_MUSIC_DIRECTORY')

    def PlayerSize(self) -> Tuple[int, int]:
        return self.playerSize

    def InitialMusicDirectory(self) -> str:
        return self.initialMusicDir
