import pandas as pd
from csv import reader

if __name__ == '__main__':

    all_fives = []

    data_files_names = ['all_fives_p1, all_fives_p2']

    for data_file_name in data_files_names:
        with open(f'serial_data/{data_file_name}.csv', 'r') as file:
            data = reader(file)
            for row in data:
                all_fives.append(row)


