from money.expression import Expression


class Money(Expression):
    def __init__(self, amount, currency):
        self._currency = currency
        self._amount = amount

    def __eq__(self, other):
        return self.amount == other.amount \
               and self.currency == other.currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def plus(self, addend):
        return Money(self.amount + addend.amount, self.currency)

    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency

