"""
@author: David Lei
@since: 18/10/2017

"""
import string
import random

def random_lowercase_strings_generator(number_of_strings=1, max_length=100):
    """Returns a generator of strings (looks like an array of strings)."""
    for _ in range(number_of_strings):
        length = random.randint(1, max_length)
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        yield s

def random_integer_array_generator(lower_bound_inclusive=0, upper_bound_inclusive=1000,
                                   integers_per_array=100, number_of_arrays=100):
    """Returns a generator of integer arrays."""
    for _ in range(number_of_arrays):
        int_array = [random.randint(lower_bound_inclusive, upper_bound_inclusive) for _ in range(integers_per_array)]
        yield int_array

if __name__ == "__main__":
    print("mucking around with random string generator.")
    string_gen = random_lowercase_strings_generator(number_of_strings=10, max_length=10)
    for s in string_gen:
        print(s)
    print(list(random_lowercase_strings_generator(number_of_strings=10, max_length=10)))

    print("\nmucking around with random integer array generator.")
    arrays = random_integer_array_generator(lower_bound_inclusive=0, upper_bound_inclusive=1000,
                                            integers_per_array=5, number_of_arrays=3)
    for array in arrays:
        print(array)
    print(list(random_integer_array_generator(lower_bound_inclusive=0, upper_bound_inclusive=1000,
                                              integers_per_array=5, number_of_arrays=3)))