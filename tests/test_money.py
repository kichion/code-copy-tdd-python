import unittest

from nose.tools import eq_, assert_true, assert_false

from bank import Bank
from money.factory import MoneyFactory
from sum import Sum


class TestMoneyMethods(unittest.TestCase):
    def test_multiplication(self):
        five = MoneyFactory.dollar(5)
        eq_(MoneyFactory.dollar(10), five.times(2))
        eq_(MoneyFactory.dollar(15), five.times(3))

    def test_equality(self):
        assert_true(MoneyFactory.dollar(5).__eq__(MoneyFactory.dollar(5)))
        assert_false(MoneyFactory.dollar(5).__eq__(MoneyFactory.dollar(3)))
        assert_false(MoneyFactory.franc(5).__eq__(MoneyFactory.dollar(5)))

    def test_currency(self):
        assert_true('USD', MoneyFactory.dollar(1).currency)
        assert_true('CHF', MoneyFactory.franc(1).currency)

    def test_simple_addition(self):
        five = MoneyFactory.dollar(5)
        sum_ = five.plus(MoneyFactory.dollar(5))
        bank = Bank()
        reduced = bank.reduce(sum_, 'USD')
        eq_(MoneyFactory.dollar(10), reduced)

    def test_plus_return_sum(self):
        five = MoneyFactory.dollar(5)
        result = five.plus(five)
        sum_ = result
        eq_(five, sum_.augend)
        eq_(five, sum_.addend)

    def test_reduce_sum(self):
        sum_ = Sum(MoneyFactory.dollar(5), MoneyFactory.dollar(4))
        bank = Bank()
        result = bank.reduce(sum_, 'USD')
        eq_(MoneyFactory.dollar(7), result)

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(MoneyFactory.dollar(1), 'USD')
        eq_(MoneyFactory.dollar(1), result)


if __name__ == '__main__':
    unittest.main()
