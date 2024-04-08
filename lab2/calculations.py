class Calculations:

    def calculate_mean(self, numbers: list[float]) -> float:
        return sum(numbers) / len(numbers)

    def calculate_variance(self, numbers: list[float]) -> float:
        mean = self.calculate_mean(numbers)
        total_sum = sum((num - mean) ** 2 for num in numbers)
        return total_sum / (len(numbers))

    def _is_inside_circle(self, x: float, y: float, R: float, S: tuple[float, float]) -> bool:
        a, b = S
        return (x - a) ** 2 + (y - b) ** 2 <= R ** 2

    def monte_carlo_circles_area(self, points: list[tuple[float, float]], R: float, r: float) -> float:
        count_inside = 0
        S: tuple[float, float] = (0, R)
        s: tuple[float, float] = (R, 0)

        for point in points:
            x, y = point
            if self._is_inside_circle(x, y, R, S) and self._is_inside_circle(x, y, r, s):
                count_inside += 1

        ratio = count_inside / len(points)

        square_area = (2 * R) ** 2
        estimated_area = ratio * square_area

        return estimated_area
