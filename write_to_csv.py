import csv
import random
from managers.utils import random_string

if __name__ == '__main__':
    with open('given_values.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for i in range(1000):
            csv_writer.writerow(
                [random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000), random_string(15)])
