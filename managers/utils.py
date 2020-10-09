import random
import string


def random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def swap(given_array, first_elem, second_elem):
    given_array[first_elem], given_array[second_elem] = given_array[second_elem], given_array[first_elem]
