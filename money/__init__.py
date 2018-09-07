from abc import abstractmethod, ABCMeta


class Money(metaclass=ABCMeta):
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount \
               and type(self) == type(other)

    @abstractmethod
    def times(self, multiplier):
        pass
