import unittest

from nose.tools import eq_, assert_true, assert_false

from money import Money
from money.factory import MoneyFactory


class TestMoneyMethods(unittest.TestCase):
    def test_multiplication(self):
        five = MoneyFactory.dollar(5)
        eq_(MoneyFactory.dollar(10), five.times(2))
        eq_(MoneyFactory.dollar(15), five.times(3))

    def test_equals(self):
        assert_true(MoneyFactory.dollar(5).__eq__(MoneyFactory.dollar(5)))
        assert_false(MoneyFactory.dollar(5).__eq__(MoneyFactory.dollar(3)))
        assert_true(MoneyFactory.franc(5).__eq__(MoneyFactory.franc(5)))
        assert_false(MoneyFactory.franc(5).__eq__(MoneyFactory.franc(3)))
        assert_false(MoneyFactory.franc(5).__eq__(MoneyFactory.dollar(5)))

    def test_franc_multiplication(self):
        five = MoneyFactory.franc(5)
        eq_(MoneyFactory.franc(10), five.times(2))
        eq_(MoneyFactory.franc(15), five.times(3))

    def test_currency(self):
        assert_true('USD', MoneyFactory.dollar(1).currency)
        assert_true('CHF', MoneyFactory.franc(1).currency)

    def test_different_class_equals(self):
        assert_true(Money(10, 'CHF').__eq__(MoneyFactory.franc(10)))


if __name__ == '__main__':
    unittest.main()
