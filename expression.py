from abc import abstractmethod


class Expression:
    @abstractmethod
    def plus(self, addend):
        pass

    @abstractmethod
    def reduce(self, bank, to):
        pass
