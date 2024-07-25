import csv


def read_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


class FoodData:

    # reading food data from csv
    def __init__(self, data):
        self.data = read_csv('csv/Mobile_Food_Facility_Permit.csv')
        self.data = [dict(zip(self.data[0], row)) for row in self.data]
        self.data = self.data[1:]

