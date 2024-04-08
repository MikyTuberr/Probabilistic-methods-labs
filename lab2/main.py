from linear_generator import LinearGenerator as lg
from prob_dist_verifier import ProbDistVerifier as pdv
from calculations import Calculations as calc
from shift_register_generator import ShiftRegisterGenerator as sg


def main():
    lin_gen = lg()
    reg_gen = sg(L=64, p=10, q=3)
    verifier = pdv()
    cal = calc()

    x_points: list[float] = lin_gen.generate(a=397204094, c=0, M=2 ** 31 - 1, n=100000)
    y_points: list[float] = lin_gen.generate(a=397204094, c=0, M=2 ** 31 - 1, n=100000)
    print(verifier.verify(x_points))
    print(verifier.verify(y_points))

    points: list[tuple:[float, float]] = list(zip(y_points, x_points))
    area = cal.monte_carlo_circles_area(points, R=1, r=0.5)
    print(area)

    numbers = reg_gen.generate(N=1000)
    print(verifier.verify(numbers))

    tosses = reg_gen.simulate_coin_tosses(N=5000)

    K: int = 5
    sequence: list[int] = [1] * K
    count: int = 0
    for i in range(len(tosses) - K + 1):
        if tosses[i:i+K] == sequence:
            count += 1

    prob: float = count / (len(tosses) - K + 1)
    print(tosses)
    print(prob)


if __name__ == '__main__':
    main()
