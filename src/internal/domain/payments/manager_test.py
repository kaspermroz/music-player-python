from pytest import raises

from src.internal.domain.payments.manager import PaymentsManager, CurrencyMismatchError, ChangeError
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
from src.internal.domain.money import Money
from src.internal.domain.currency import PLN, EUR
from src.tests.fixtures import SomeMoney


def test_payments_manager_add_coins():
    pm = PaymentsManager(PLN)

    pm.AddCoin(Coin1PLN)

    assert pm.CoinsIn()[0] is Coin1PLN

    coin1EUR = Coin(Money("1", EUR))

    with raises(CurrencyMismatchError) as err:
        pm.AddCoin(coin1EUR)

    assert err.value.message == "currency mismatch: allowed: PLN, actual: EUR"


def test_payments_manager_get_change():
    pm = PaymentsManager(PLN)

    pm.AddCoin(Coin5PLN)
    pm.AddCoin(Coin5PLN)
    pm.AddCoin(Coin5PLN)
    pm.AddCoin(Coin5PLN)
    pm.AddCoin(Coin2PLN)

    change = pm.GetChange(SomeMoney())

    assert len(change) == 4
    assert change[0] is Coin50GR
    assert change[1] is Coin10GR
    assert change[2] is Coin2GR
    assert change[3] is Coin1GR
    assert len(pm.CoinsIn()) == 0


def test_payments_manager_get_change_exception():
    pm = PaymentsManager(PLN)

    with raises(ChangeError) as err:
        pm.GetChange(SomeMoney())

    assert err.value.message == "paid amount is bigger than sum of coins in [0 PLN < 21.37 PLN]"
