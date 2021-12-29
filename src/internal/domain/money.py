from decimal import Decimal, getcontext

from currency import Currency


class Money:
    amount: Decimal
    currency: Currency

    def __init__(self, amount: str, currency: Currency):
        if amount == "":
            raise TypeError("amount cannot be empty")
        if currency.IsZero():
            raise TypeError("currency cannot be empty")

        getcontext().prec = 2

        self.amount = Decimal(amount)
        self.currency = currency

    def Amount(self) -> Decimal:
        return self.amount

    def Currency(self) -> Currency:
        return self.currency

    def Equal(self, m) -> bool:
        return self.amount.compare(m.Amount()) == 0 and self.currency == m.Currency()

    def Add(self, m: Decimal):
        self.amount = self.amount + m
