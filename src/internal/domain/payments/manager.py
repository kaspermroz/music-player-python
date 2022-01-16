from typing import List
from decimal import Decimal
from src.internal.domain.money import Money, MoneyZero
from src.internal.domain.currency import Currency
from src.internal.domain.payments.coin import Coin, \
    Coin1GR, \
    Coin2GR, \
    Coin5GR, \
    Coin10GR, \
    Coin20GR, \
    Coin50GR, \
    Coin1PLN, \
    Coin2PLN, \
    Coin5PLN


class ChangeError(Exception):
    """
    Exception raised when local song is added to non-local playlist and the other way around
    """

    message: str

    def __init__(self, msg: str):
        self.message = msg
        super().__init__(self.message)


class CurrencyMismatchError(Exception):
    """
     Exception raised when trying to add coin with different currency then defined in constructor
     of PaymentsManager
    """

    message: str

    def __init__(self, allowed: Currency, actual: Currency):
        self.message = f"currency mismatch: allowed: {allowed}, actual: {actual}"
        super().__init__(self.message)


class PaymentsManager:
    currency: Currency
    allowedCoinsIn: List[Coin]
    allowedCoinsOut: List[Coin]
    sumIn: Money
    credit: Money

    def __init__(self, cur: Currency):
        self.currency = cur
        self.allowedCoinsIn = [
            Coin10GR,
            Coin20GR,
            Coin50GR,
            Coin1PLN,
            Coin2PLN,
            Coin5PLN,
        ]
        self.allowedCoinsOut = [
            Coin1GR,
            Coin2GR,
            Coin5GR,
            Coin10GR,
            Coin20GR,
            Coin50GR,
            Coin1PLN,
            Coin2PLN,
            Coin5PLN,
        ]
        self.coinsIn = []
        self.sumIn = self.moneyZero()
        self.credit = self.moneyZero()

    def CoinsIn(self) -> List[Coin]:
        return self.coinsIn

    def AddMoney(self, m: Money):
        if self.credit > self.moneyZero():
            if self.credit >= m:
                self.credit -= m
            else:
                self.sumIn = m - self.credit
                self.credit = self.moneyZero()
        else:
            self.sumIn += m

    def AddCoin(self, c: Coin):
        if c.Value().Currency() != self.currency:
            raise CurrencyMismatchError(self.currency, c.Value().Currency())

        self.AddMoney(c.Value())

    def AddCredit(self, amount: Money):
        if self.sumIn > self.moneyZero():
            if self.sumIn >= amount:
                self.sumIn -= amount
            else:
                self.credit = amount - self.sumIn
                self.sumIn = self.moneyZero()
        else:
            self.credit += amount

    def GetChange(self, paid: Money) -> List[Coin]:
        if self.sumIn < paid:
            raise ChangeError(
                f"paid amount is bigger than sum of coins in [{self.sumIn} < {paid}]"
            )

        change = self.sumIn - paid
        self.sumIn -= paid
        coins = []

        while change > Money("0", self.currency):
            c = getBiggestCoin(change)
            coins.append(c)
            change -= c.Value()

        return coins

    def SumIn(self) -> Money:
        return self.sumIn

    def Credit(self) -> Money:
        return self.credit

    def moneyZero(self) -> Money:
        return MoneyZero(self.currency)


def getBiggestCoin(amount: Money):
    if amount >= Coin5PLN.Value():
        return Coin5PLN
    elif amount >= Coin2PLN.Value():
        return Coin2PLN
    elif amount >= Coin1PLN.Value():
        return Coin1PLN
    elif amount >= Coin50GR.Value():
        return Coin50GR
    elif amount >= Coin20GR.Value():
        return Coin20GR
    elif amount >= Coin10GR.Value():
        return Coin10GR
    elif amount >= Coin5GR.Value():
        return Coin5GR
    elif amount >= Coin2GR.Value():
        return Coin2GR
    elif amount >= Coin1GR.Value():
        return Coin1GR
    else:
        return Decimal(0)
