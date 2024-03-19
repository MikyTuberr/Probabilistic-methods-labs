from DataParser import DataParser as dp
from Permutations import Permutations as per
from Combinations import Combinations as com
import math
from typing import Tuple

def calculate_distance(city1: list, city2: list) -> float:
    lat1, lon1 = float(city1[3]), float(city1[4])
    lat2, lon2 = float(city2[3]), float(city2[4])
    return ((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2) ** 0.5

def find_shortest_path(all_permutations: list) -> Tuple[list, float]:
    min_distance = float('inf')
    for path in all_permutations:
        distance = sum(calculate_distance(path[i], path[i + 1]) for i in range(len(path) - 1))
        if distance < min_distance:
            min_distance = distance
            best_path = path
    return best_path, min_distance

def find_closest_subset(cities: list, K: int) -> list:
    max_population = sum(int(city[2]) for city in cities) / 2
    min_diff = math.inf
    closest_subset = None

    for c in com.generate(cities, K):
        subset_population = sum(int(city[2]) for city in c)
        diff = abs(subset_population - max_population)
        if diff < min_diff:
            min_diff = diff
            closest_subset = c
    return closest_subset


def main():
    data = dp.parse_data("miasta.in")
    N = 6  
    cities = data[:N]

    all_permutations = per.generate(cities)
    for p in all_permutations:
        print(p)

    K = N//2

    best_path, min_distance = find_shortest_path(all_permutations)
    print("Najkrotsza trasa:", [city[1] for city in best_path], "Dlugosc:", min_distance)
    combinations = com.generate(cities, K)
    for c in combinations:
        print(c)

    closest_subset = find_closest_subset(cities, K)
    print("Podzbior K=N/2 najblizszy 50% populacji:")
    for city in closest_subset:
        print(city[1], "->", city[2], "mieszkancow")

   

if __name__ == '__main__':
    main()
