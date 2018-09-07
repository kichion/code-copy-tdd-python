from money import Money


class Dollar:
    def __init__(self, amount):
        self.money = Money(amount)

    def times(self, multiplier):
        return Dollar(self.money._amount * multiplier)

    def __eq__(self, other):
        return self.money == other.money
