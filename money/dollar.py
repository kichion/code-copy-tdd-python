from money import Money


class Dollar(Money):
    def __init__(self, amount):
        super(Dollar, self).__init__(amount, 'USD')

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)
