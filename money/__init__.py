from expression import Expression


class Pair:
    def __init__(self, from_, to):
        self.from_ = from_
        self.to = to

    def __eq__(self, other):
        return self.from_ == other.from_ and self.to == other.to

    def __hash__(self):
        return 0


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to):
        amount = self.augend.reduce(bank, to).amount \
                 + self.addend.reduce(bank, to).amount
        return Money(amount, to)

    def plus(self, addend):
        return Sum(self, addend)

    def times(self, multiplier):
        return Sum(self.augend.times(multiplier), self.augend.times(multiplier))


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
        return Sum(self, addend)

    def reduce(self, bank, to):
        rate = bank.rate(self.currency, to)
        return Money(self.amount / rate, to)

    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency

