class Singleton(type):
    """
    Abstract class to ensure only one instance of child class
    Usage:

    class Children(metaclass=Singleton):
        ...

    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]
