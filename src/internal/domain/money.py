from decimal import Decimal, getcontext

from src.internal.domain.currency import Currency


class Money:
    amount: Decimal
    currency: Currency

    def __init__(self, amount: str, currency: Currency):
        if amount == "":
            raise TypeError("amount cannot be empty")
        if Decimal(amount) < Decimal(0):
            raise TypeError("amount cannot be negative")
        if currency.IsZero():
            raise TypeError("currency cannot be empty")

        getcontext().prec = 2

        self.amount = Decimal(amount)
        self.currency = currency

    def __lt__(self, other) -> bool:
        return self.Currency() == other.Currency() and self.Amount() < other.Amount()

    def __le__(self, other) -> bool:
        return self.Currency() == other.Currency() and self.Amount() <= other.Amount()

    def __gt__(self, other) -> bool:
        return self.Currency() == other.Currency() and self.Amount() > other.Amount()

    def __ge__(self, other) -> bool:
        return self.Currency() == other.Currency() and self.Amount() >= other.Amount()

    def __add__(self, other):
        return Money(str(self.Amount() + other.Amount()), self.Currency())

    def __sub__(self, other):
        return Money(str(self.Amount() - other.Amount()), self.Currency())

    def __str__(self):
        return f"{self.Amount()} {self.Currency()}"

    def Amount(self) -> Decimal:
        return self.amount

    def Currency(self) -> Currency:
        return self.currency

    def Equal(self, m) -> bool:
        return self.amount.compare(m.Amount()) == 0 and self.currency == m.Currency()

    def Add(self, m: Decimal):
        self.amount = self.amount + m
