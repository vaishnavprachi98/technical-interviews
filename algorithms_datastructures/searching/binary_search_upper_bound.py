"""
@author: David Lei
@since: 19/10/2017

"""

def upper_bound_binary_search(array, target):
    hi = len(array) - 1
    lo = 0
    while lo <= hi:
        mid = (hi + lo) // 2
        if array[mid] == target:
            # We know at index mid the target exists, search to the right of this, by changing lo.
            lo = mid + 1
        elif array[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    # Last value in mid is where we can insert the element without breaking ordering.
    return lo

if __name__ == "__main__":
    # index: 0  1  2  3  4  5  6  7  8  9  10  11
    array = [1, 2, 3, 4, 5, 5, 5, 6, 7, 9, 15, 17]

    target = 5
    upper_bound = upper_bound_binary_search(array, target)
    print(upper_bound)
    if upper_bound != 7:
        print("first call on target 5, upper bound should be 7")
    else:
        print("Yay correct upper bound of 7 for target 5")
    array.insert(upper_bound, target)
    print(array)

    target = 5
    upper_bound = upper_bound_binary_search(array, target)
    print(upper_bound)
    if upper_bound != 8:
        print("first call on target 5, upper bound should be 8")
    else:
        print("Yay correct upper bound of 8 for target 5")
    array.insert(upper_bound, target)
    print(array)

    print("\nDoing same tests as lower bound")

    target = 100
    upper_bound = upper_bound_binary_search(array, target)
    print(upper_bound)
    array.insert(upper_bound, target)
    print(array)

    target = 5
    upper_bound = upper_bound_binary_search(array, target)
    print(upper_bound)
    array.insert(upper_bound, target)
    print(array)

    target = 10
    upper_bound = upper_bound_binary_search(array, target)
    print(upper_bound)
    array.insert(upper_bound, target)
    print(array)

    target = 6
    upper_bound = upper_bound_binary_search(array, target)
    print(upper_bound)
    array.insert(upper_bound, target)
    print(array)

    target = 5
    upper_bound = upper_bound_binary_search(array, target)
    print(upper_bound)
    array.insert(upper_bound, target)
    print(array)

    copied = array[::]
    copied.sort()
    if array == copied:
        print("Yay ordering did not break")
    else:
        print("Ya stuffed up mate")