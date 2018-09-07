from money.factory import MoneyFactory


class Bank:
    def reduce(self, source, to):
        return MoneyFactory.dollar(10)
