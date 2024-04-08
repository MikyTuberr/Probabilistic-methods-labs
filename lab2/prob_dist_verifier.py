from calculations import Calculations


class ProbDistVerifier:
    def __init__(self):
        self.proper_mean = 0.5
        self.proper_variance = 1 / 12

    def verify(self, numbers: list[float]) -> bool:
        calc = Calculations()
        mean = calc.calculate_mean(numbers)
        variance = calc.calculate_variance(numbers)
        return self._check_variance(variance) and self._check_mean(mean)

    def _check_mean(self, mean: float) -> bool:
        diff = round(abs(mean - self.proper_mean), 2)
        return diff < 0.1

    def _check_variance(self, variance: float) -> bool:
        diff = round(abs(variance - self.proper_variance), 2)
        return diff < 0.1
