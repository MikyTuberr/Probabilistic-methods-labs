import csv

class DataParser:
    @staticmethod
    def parse_data(file_name: str) -> list:
        data = []
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ')
            next(reader)
            for row in reader:
                data.append(row)
        return data