__author__ = 'David'

'''
if item == middle
    found
else if item < middle
    search left half
else
    search right half
'''
# PRECONDITION: list has to be sorted
# log N --> better than linear
# best = O(1)
# worst = O(log n)
# divide and decrease problem
# mid = low+high // 2
# list = 1,2,3,4,5
# len = 5, low = 0, high = 4
# mid is manipulated by changing low and high, so needs to be calculated using it

def binarySearch_Iterative(list, item):
    # ITERATIVE METHOD
    # specify range of possible positions
    low = 0
    high = len(list) -1
    while low <= high:
        mid = (low+high) // 2
        # found
        if item == list[mid]:
            return mid
        # look in lower
        elif item < list[mid]:
            high = mid-1
        # look in upper
        else:
            low = mid+1
    return -1                   # catches inputs of []

#print(binarySearch_Iterative([1,2,3,5], 9))

def binarySearch_Recursive(list, item, low=0, high=-1):
    # RECURSIVE method
    if not list:                # list = [] --> not list, for inputs of []
        print("idk")
        return -1

    if high == -1:
        high = len(list) -1

    if low == high:
        if list[low] == item:
            return low
        else:
            return -1

    if high < low:
        # value not in list
        return -1

    mid = (low+high)//2

    if item == list[mid]:
        return mid
    elif item < list[mid]:
        return binarySearch_Recursive(list, item, low, mid-1)  # mid not included, python up to not included
    else:
        return binarySearch_Recursive(list, item, mid+1, high)  # mid included

#print(binarySearch_Recursive([1,2,3,5], 4))


# tute use binary search to find square root of 2
def binary_search_root2(find, min, max):
    # find square root of 2 using binary search
    if max < min:
        return -1
    else:
        mid = (max + min)/2

        if round(mid*mid, 10) == find:
            return mid
        elif mid*mid > find:
            return binary_search_root2(find, min, mid)
        elif mid*mid < find:
            return binary_search_root2(find, mid, max)


#print(binary_search_root2(2, 0, 2))


def test_listsplits():
    # works as intended
    list = [1,2,3,4,5,6,7]
    mid = len(list)//2
    midItem = list[mid]
    # list up to not including mid
    lower = list[:mid]
    # list including mid till end
    upper = list[mid:]
    print(midItem)
    print(lower)
    print(upper)

#test_listsplits()

'''
NOTE: Private method
put underscore in front of method i.e
_binary_search
something you don't expect people to use while using your class
but the class can use
'''


def myBinarySearch(list, item):
    if len(list) == 0:
        return -1
    else:
        mid = len(list)//2
        if list[mid] == item:
            return mid
        else:
            if item < list[mid]:
                return myBinarySearch(list[:mid], item)
            else:
                return myBinarySearch(list[mid+1:], item)

print(myBinarySearch([1,2,3,4,5,7,8,10], 9))
