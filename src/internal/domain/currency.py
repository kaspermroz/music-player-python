class Currency:
    s: str

    def __init__(self, currency: str):
        if currency == "":
            raise TypeError("currency cannot be empty")

        self.s = currency

    def __str__(self):
        return self.String()

    def __eq__(self, other) -> bool:
        return self.String() == other.String()

    def String(self) -> str:
        return self.s

    def IsZero(self) -> bool:
        return self.s == ""


PLN = Currency("PLN")
EUR = Currency("EUR")
