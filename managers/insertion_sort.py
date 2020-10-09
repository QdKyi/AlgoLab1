from managers.utils import swap


class InsertionSort:
    def __init__(self):
        self.counter_of_comparison_operations = 0
        self.counter_of_swap_operations = 0

    def insertion_sort(self, given_array, compare_function):

        for i in range(1, len(given_array)):
            current_value = given_array[i]
            current_position = i

            while current_position > 0 and compare_function(given_array[current_position - 1], current_value):
                swap(given_array, current_position, current_position - 1)
                current_position = current_position - 1

                self.counter_of_swap_operations += 1
                self.counter_of_comparison_operations += 2

        print(f'InsertionSort:\n'
              f'Number of compares = {self.counter_of_comparison_operations}\n'
              f'Number of swaps = {self.counter_of_swap_operations}')
