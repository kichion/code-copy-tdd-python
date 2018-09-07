from money import Money


class Franc(Money):
    def __init__(self, amount):
        super(Franc, self).__init__(amount, 'CHF')

    def times(self, multiplier):
        return Franc(self._amount * multiplier)
