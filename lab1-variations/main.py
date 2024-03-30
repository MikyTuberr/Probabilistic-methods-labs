from Variations import Variations as v
from DataParser import DataParser as dp
from Calculations import Calculations as c


def main() -> None:
    data = dp.parse_data("cities.in")

    N = 5
    data = data[:5]

    var_no_repeats = v.generate_no_repeats(data, 3)
    #print_result(var_no_repeats)
    [best_path, distance] = c.find_shortest_path(var_no_repeats)
    print("path:",best_path)
    print("distance:", distance)
    
    var_repeats = v.generate_repeats(data, 3)
    #print_result(var_repeats)
    [cities, best_avg] = c.find_highest_avg_pop(var_no_repeats)
    print("cities:",cities)
    print("average:", best_avg)
    

if __name__ == "__main__":
    main()

