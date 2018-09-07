from money import Money


class Franc(Money):
    def __init__(self, amount, currency):
        super(Franc, self).__init__(amount, currency)
