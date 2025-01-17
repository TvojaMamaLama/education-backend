import pytest

from banking.selector import BankSelector
from stripebank.bank import StripeBank
from tinkoff.bank import TinkoffBank
from tinkoff.credit import TinkoffCredit


@pytest.fixture
def select():
    return BankSelector()


@pytest.mark.parametrize(('desired', 'result'), [
    ('tinkoff_bank', TinkoffBank),
    ('tinkoff_credit', TinkoffCredit),
    ('stripe', StripeBank),
    ('ev1l', TinkoffBank),
    ('', TinkoffBank),
])
def test(select, desired, result):
    assert select(desired) == result


def test_default_bank(select):
    assert select() == TinkoffBank
