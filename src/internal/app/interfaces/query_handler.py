from abc import ABC


class QueryHandler(ABC):
    """
    Standard query interface, used for reading
    """
    def __init__(self, **_kwargs):
        pass

    def QueryName(self) -> str:
        raise NotImplementedError

    def Execute(self, *_args, **_kwargs) -> any:
        raise NotImplementedError
