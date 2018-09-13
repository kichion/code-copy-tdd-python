from money import Pair


class Bank:
    rates = {}

    def reduce(self, source, to):
        return source.reduce(self, to)

    def add_rate(self, from_, to, rate):
        self.rates[Pair(from_, to)] = rate

    def rate(self, from_, to):
        if from_ == to:
            return 1
        return self.rates.get(Pair(from_, to))
