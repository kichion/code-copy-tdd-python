import unittest

from nose.tools import eq_, assert_true, assert_false

from dollar import Dollar
from franc import Franc


class TestMoneyMethods(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        eq_(Dollar(10), five.times(2))
        eq_(Dollar(15), five.times(3))

    def test_equals(self):
        assert_true(Dollar(5).__eq__(Dollar(5)))
        assert_false(Dollar(5).__eq__(Dollar(3)))

    def test_franc_multiplication(self):
        five = Franc(5)
        eq_(Franc(10), five.times(2))
        eq_(Franc(15), five.times(3))


if __name__ == '__main__':
    unittest.main()
