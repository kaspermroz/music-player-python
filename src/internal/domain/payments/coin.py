from src.internal.domain.money import Money
from src.internal.domain.currency import PLN


class Coin:
    """
    Domain model for coins used by GUI and PaymentsManager
    """
    value: Money

    def __init__(self, value: Money):
        self.value = value

    def Value(self) -> Money:
        return self.value


Coin1GR = Coin(Money("0.01", PLN))
Coin2GR = Coin(Money("0.02", PLN))
Coin5GR = Coin(Money("0.05", PLN))
Coin10GR = Coin(Money("0.10", PLN))
Coin20GR = Coin(Money("0.20", PLN))
Coin50GR = Coin(Money("0.50", PLN))

Coin1PLN = Coin(Money("1.00", PLN))
Coin2PLN = Coin(Money("2.00", PLN))
Coin5PLN = Coin(Money("5.00", PLN))
