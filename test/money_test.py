from nose.tools import eq_

from money import Dollar


def test_multiplication() -> None:
    five = Dollar(5)
    five.times(2)
    eq_(10, five.amount)
