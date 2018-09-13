from abc import abstractmethod


class Expression:
    @abstractmethod
    def reduce(self, bank, to):
        pass
