from random import shuffle
from managers.utils import swap


class QuickSort:
    def __init__(self):
        self.counter_of_comparison_operations = 0
        self.counter_of_swap_operations = 0

    def partition(self, given_array, start, end, compare_function):
        pivot = given_array[start]
        low = start + 1
        high = end

        while True:

            while low <= high and compare_function(given_array[high], pivot):
                self.counter_of_comparison_operations += 2
                high = high - 1

            while low <= high and not compare_function(given_array[low], pivot):
                self.counter_of_comparison_operations += 2
                low = low + 1
            self.counter_of_comparison_operations += 1
            if low <= high:
                swap(given_array, low, high)

                self.counter_of_swap_operations += 1
            else:
                break
        swap(given_array, start, high)
        self.counter_of_swap_operations += 1

        return high

    def quick_sort(self, given_array, start, end, compare_function):
        if start >= end:
            return

        my_partition = self.partition(given_array, start, end, compare_function)

        self.quick_sort(given_array, start, my_partition - 1, compare_function)
        self.quick_sort(given_array, my_partition + 1, end, compare_function)

    def sort(self, given_array, compare_function):
        self.counter_of_comparison_operations = 0
        self.counter_of_swap_operations = 0

        shuffle(given_array)

        self.quick_sort(given_array, 0, len(given_array) - 1, compare_function)

        print(f'QuickSort:\n'
              f'Number of compares = {self.counter_of_comparison_operations}\n'
              f'Number of swaps = {self.counter_of_swap_operations}')
