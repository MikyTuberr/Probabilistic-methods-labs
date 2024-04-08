from random import randint


class ShiftRegisterGenerator:
    def __init__(self, L: int, p: int, q: int):
        self.L = L
        self.p = p
        self.q = q
        self.register: list[int] = [randint(0, 1) for _ in range(L)]

    def _generate_bit(self) -> int:
        bit = self.register[-self.p] ^ self.register[-self.q]
        self.register.pop(0)
        self.register.append(bit)
        return bit

    def _generate_number(self) -> float:
        return sum(self._generate_bit() * (2 ** -i) for i in range(1, self.L + 1))

    def generate(self, N: int) -> list[float]:
        return [self._generate_number() for _ in range(N)]

    def simulate_coin_tosses(self, N: int) -> list[int]:
        return [self._generate_bit() for _ in range(N)]
