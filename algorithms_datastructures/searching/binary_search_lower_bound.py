"""
@author: David Lei
@since: 19/10/2017

"""

def lower_bound_binary_search(array, target):
    hi = len(array) - 1
    lo = 0
    while lo <= hi:
        mid = (hi + lo) // 2
        if array[mid] == target:
            # We know at index mid the target exists, search to the left of this.
            # We keep searching until L < mid < target where mid is < target
            # once we get hi pointing to the first element < target then every element encountered by array[(hi+lo)//2]
            # will be < target so the bottom half will be continuously discarded until lo > hi.
            # when lo > hi as we know hi will be pointing to the first occurrence of a number < target lo is pointing to the
            # first occurrence of the target so return lo.
            # Note: not always the case were at which lo == mid + 1
            hi = mid - 1
        elif array[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    # Last value in mid is where we can insert the element without breaking ordering.
    # print("lo: %s, hi: %s, mid: %s" % (lo, hi, mid))
    return lo

if __name__ == "__main__":
    # index: 0  1  2  3  4  5  6  7  8  9  10  11
    array = [1, 2, 3, 4, 5, 5, 5, 6, 7, 9, 15, 17]
    target = 100
    lower_bound = lower_bound_binary_search(array, target)
    print(lower_bound)
    array.insert(lower_bound, target)
    print(array)

    target = 5
    lower_bound = lower_bound_binary_search(array, target)
    print(lower_bound)
    array.insert(lower_bound, target)
    print(array)

    target = 10
    lower_bound = lower_bound_binary_search(array, target)
    print(lower_bound)
    array.insert(lower_bound, target)
    print(array)

    target = 6
    lower_bound = lower_bound_binary_search(array, target)
    print(lower_bound)
    array.insert(lower_bound, target)
    print(array)

    target = 5
    lower_bound = lower_bound_binary_search(array, target)
    print(lower_bound)
    array.insert(lower_bound, target)
    print(array)

    copied = array[::]
    copied.sort()
    if array == copied:
        print("Yay ordering did not break")
    else:
        print("Ya stuffed up mate")