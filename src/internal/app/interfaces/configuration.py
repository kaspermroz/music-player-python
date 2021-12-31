from typing import Tuple
from abc import ABC


class Configuration(ABC):
    """Configuration interface for the service"""

    def PlayerSize(self) -> Tuple[int, int]:
        raise NotImplementedError

    def InitialMusicDirectory(self) -> str:
        raise NotImplementedError
