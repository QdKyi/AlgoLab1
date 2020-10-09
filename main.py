import time
import csv

from models import bicycle
from managers import quick_sort
from managers import insertion_sort

if __name__ == '__main__':
    bicycle_array = []

    with open('given_values.csv', 'r') as file:

        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            bicycle_array.append(bicycle.Bicycle(number_of_gears=row[0], weight_in_kg=row[1],
                                                 max_weight=row[2], producer_name=row[3]))

    my_quick_sort = quick_sort.QuickSort()

    quick_sort_start_time = time.time()
    my_quick_sort.sort(bicycle_array, compare_function=lambda o1, o2: o1.weight_in_kg < o2.weight_in_kg)
    quick_sort_end_time = time.time()

    print(f'Array after QuickSort: {bicycle_array}')
    print(f'QuickSort run time: {quick_sort_end_time - quick_sort_start_time} seconds\n')

    my_insertion_sort = insertion_sort.InsertionSort()

    insertion_sort_start_time = time.time()
    my_insertion_sort.insertion_sort(bicycle_array,
                                     compare_function=lambda o1, o2: o1.number_of_gears < o2.number_of_gears)
    insertion_sort_end_time = time.time()

    print(f'Array after InsertionSort: {bicycle_array}')
    print(f'InsertionSort run time: {insertion_sort_end_time - insertion_sort_start_time} seconds')
