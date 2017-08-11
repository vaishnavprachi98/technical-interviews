"""
@author: David Lei
@since: 26/08/2016
@modified: 22/4/2017

Note: Didn't bother handling recusion depth reached.
"""


def binary_search_find_root(number, min, max, accuracy, n):
    """
    Use to find nth dimension root of number using binary search.

    Precondition: max > min.
    Precondition: number < max

    :param number: Number to find square root of.
    :param min: lower bound, start at 0.
    :param max: upper bound, max value of number.
    :param accuracy: accuracy to round to for decimal points.
    :param n: nth dimension root to find (square = 2, cube = 3, 4, 5 .. n)
    :return:
    """
    if max <= min:  # Can't find
        return -1

    mid_val = (max + min)/2  # Returns a float.
    if round(mid_val ** n, accuracy) == number:
        return mid_val
    elif mid_val ** n > number:  # Need to make mid_val**2 less so it matches number.
        return binary_search_find_root(number, min, mid_val, accuracy, n)  # Look at values between min and mid, discard > mid point.
    elif mid_val ** n < number:
        return binary_search_find_root(number, mid_val, max, accuracy, n)  # Discard values lower than mid to make number bigger.

root_to_find_from_number = 26
min = 0
max = 100000000  # Max number range, number needs to be < max.
accuracy = 15
nth_dimension_root = 4

print(
    binary_search_find_root(root_to_find_from_number, min, max, accuracy, nth_dimension_root)
)

"""
root_to_find_number = 3
accuracy = 1
1.7229467630386353

accuracy = 2
1.7316779121756554

accuracy = 10
1.73205080757511

accuracy = 25
1.7320508075688772

Gets slightly closer every time, ~ 20 reaches recursion depth.
"""