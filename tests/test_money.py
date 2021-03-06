import unittest

from nose.tools import eq_, assert_true, assert_false

from bank import Bank
from money import Sum
from money.factory import MoneyFactory


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
        eq_(MoneyFactory.dollar(9), result)

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(MoneyFactory.dollar(1), 'USD')
        eq_(MoneyFactory.dollar(1), result)

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result = bank.reduce(MoneyFactory.franc(2), 'USD')
        eq_(MoneyFactory.dollar(1), result)

    def test_identity_rate(self):
        eq_(1, Bank().rate('USD', 'USD'))

    def test_mixed_addition(self):
        five_bucks = MoneyFactory.dollar(5)
        ten_francs = MoneyFactory.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result = bank.reduce(five_bucks.plus(ten_francs), 'USD')
        eq_(MoneyFactory.dollar(10), result)

    def test_sum_plus_money(self):
        five_bucks = MoneyFactory.dollar(5)
        ten_francs = MoneyFactory.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        sum_ = Sum(five_bucks, ten_francs).plus(five_bucks)
        result = bank.reduce(sum_, 'USD')
        eq_(MoneyFactory.dollar(15), result)

    def test_sum_times(self):
        five_bucks = MoneyFactory.dollar(5)
        ten_francs = MoneyFactory.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        sum_ = Sum(five_bucks, ten_francs).times(2)
        result = bank.reduce(sum_, 'USD')
        eq_(MoneyFactory.dollar(20), result)


if __name__ == '__main__':
    unittest.main()
