import random


def rand_table(table):
    y = random.random()
    result = [0] + [sum(table[:i]) for i in range(1, len(table) + 1)]

    if result[0] < y < result[1]:
        return 1
    if result[1] < y < result[2]:
        return 2
    if result[2] < y < result[3]:
        return 3
    if result[3] < y < result[4]:
        return 4


def generate_point():
    list_of_probs = [0.5, 0.2, 0.2, 0.1]
    x = rand_table(list_of_probs)

    y_table = [[0.1, 0, 0, 0.4],
               [0.2, 0, 0, 0],
               [0, 0.1, 0, 0.1],
               [0, 0, 0.1, 0]]

    rand_y = y_table[x - 1]
    results_y = [i / sum(rand_y) for i in rand_y]
    y = rand_table(results_y)
    return x, y


def main():
    n = 100000
    counter = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

    for _ in range(n):
        x, y = generate_point()
        counter[x - 1][y - 1] += 1

    print(sum([sum(r) for r in counter]))

    for r in counter:
        print(r)


if __name__ == "__main__":
    main()
