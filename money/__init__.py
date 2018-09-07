from abc import abstractmethod, ABCMeta


class Money(metaclass=ABCMeta):
    def __init__(self, amount, currency):
        self._currency = currency
        self._amount = amount

    def __eq__(self, other):
        return self.amount == other.amount \
               and type(self) == type(other)

    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency

    @abstractmethod
    def times(self, multiplier):
        pass
