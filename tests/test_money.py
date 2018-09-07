import unittest

from nose.tools import eq_

from money import Dollar


class TestMoneyMethods(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        eq_(10, product.amount)
        product = five.times(3)
        eq_(15, product.amount)


if __name__ == '__main__':
    unittest.main()
