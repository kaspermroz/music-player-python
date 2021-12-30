from abc import ABC


class Configuration(ABC):
    """Configuration interface for the service"""

    def PlayerSize(self):
        return NotImplementedError
