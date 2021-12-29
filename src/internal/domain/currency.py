class Currency:
    s: str

    def __init__(self, currency: str):
        if currency == "":
            raise TypeError("currency cannot be empty")

        self.s = currency

    def String(self) -> str:
        return self.s

    def IsZero(self) -> bool:
        return self.s == ""
