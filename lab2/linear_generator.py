class LinearGenerator:
    def __init__(self, seed: int = 42):
        self.seed = seed

    def generate(self, a: int, c: int, M: int, n: int) -> list[float]:
        result = []
        for _ in range(n):
            self.seed = (a * self.seed + c) % M
            result.append(self.seed / M)
        return result
