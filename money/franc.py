from money import Money


class Franc:
    def __init__(self, amount):
        self.money = Money(amount)

    def times(self, multiplier):
        return Franc(self.money._amount * multiplier)

    def __eq__(self, other):
        return self.money == other.money
