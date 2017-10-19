"""
@author: David Lei
@since: 19/10/2017

https://rosettacode.org/wiki/Binary_search#Python:_Library

Given a list of items find the item closest to the target value.
"""

def binary_search_closest(array, target, verbose=False):
    lo = 0
    hi = len(array) - 1
    # If we check for <= then need to check for bounds, if we just have < then need to check if mid is target index after exiting loop.
    while lo <= hi:
        mid = (lo + hi)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            lo = mid + 1
            if verbose: print("increment lo (lo: %s, hi: %s)" % (lo, hi))
        else:
            hi = mid - 1
            if verbose: print("decrement hi (lo: %s, hi: %s)" % (lo, hi))
    # Getting to here means not found, evaluate closest to the one with the least difference.
    if hi < 0:
        hi = 0
    if lo > len(array) - 1:
        lo = len(array) - 1
    lo_diff = abs(array[lo] - target)
    hi_diff = abs(array[hi] - target)
    if verbose:
        print("target %s not in array" % target)
        print("lo: %s, lo_diff: %s" % (lo, lo_diff))
        print("hi: %s, hi_diff: %s" % (hi, hi_diff))
    return lo if lo_diff < hi_diff else hi

def binary_search_rosetta(l, value):  # From rosetta code, use to test.
    low = 0
    high = len(l)-1
    while low + 1 < high:
        mid = (low+high)//2
        if l[mid] > value:
            high = mid
        elif l[mid] < value:
            low = mid
        else:
            return mid
    return high if abs(l[high] - value) < abs(l[low] - value) else low

if __name__ == "__main__":
    # indexes: 0   1  2  3  4  5  6  7  8  9
    array = [-10, -4, 0, 1, 2, 4, 5, 6, 8, 10]
    target = -11
    c1 = binary_search_closest(array, target, verbose=True)
    c2 = binary_search_rosetta(array, target)
    print("Closest:")
    print("binary_search_closest() index: %s, array[index]: %s" % (c1, array[c1]))
    print("binary_search_rosetta() index: %s, array[index]: %s"  % (c2, array[c2]))
    print("Correct: %s" % (c1 == c2))


