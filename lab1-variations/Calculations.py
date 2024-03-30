from ast import Tuple


class Calculations:

    @staticmethod
    def print_result(result: list) -> None:
        i = 1
        for r in result:
            print(i, r)
            i += 1
        print("number of elements:", len(result))

    @staticmethod
    def calculate_distance(city1: list, city2: list) -> float:
        lat1, lon1 = float(city1[3]), float(city1[4])
        lat2, lon2 = float(city2[3]), float(city2[4])

        return ((lat2 - lat1)**2 + (lon2 - lon1)**2) ** 0.5

    @staticmethod
    def calculate_avg(elements: list) -> float:
        sum_of_val = sum(int(elements[i][2]) for i in range(len(elements)))
        num_elem = len(elements)
        return sum_of_val / num_elem

    @staticmethod
    def find_shortest_path(paths: list) -> Tuple(list, float):
        best_path = []
        min_distance = float('inf')

        for path in paths:
            curr_distance = sum(Calculations.calculate_distance(path[i], path[i+1]) for i in range(len(path) - 1))
            if curr_distance < min_distance:
                min_distance = curr_distance
                best_path = path
        return best_path, min_distance

    @staticmethod
    def find_highest_avg_pop(cities: list) -> Tuple(list, float):
        biggest_city = []
        best_avg = float(0)

        for city in cities:
            curr_avg = Calculations.calculate_avg(city)
            if curr_avg > best_avg:
                best_avg = curr_avg
                biggest_city = city
        return biggest_city, best_avg
