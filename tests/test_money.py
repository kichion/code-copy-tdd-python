import unittest

from nose.tools import eq_

from money import Dollar


class TestMoneyMethods(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        eq_(10, five.amount)


if __name__ == '__main__':
    unittest.main()
