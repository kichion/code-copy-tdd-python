from money.dollar import Dollar
from money.franc import Franc


class MoneyFactory:
    @staticmethod
    def dollar(amount):
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Franc(amount, 'CHF')
