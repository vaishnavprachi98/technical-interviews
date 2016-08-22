"""
@author: David Lei
@since: 21/08/2016
@modified:

Precondition: arr is in sorted order

How it works: look at middle item in arr, if target < mid split that half and binary search it, else look at the other
                half. This reduces the search size be half each time leading to the log n complexity
Invariants: the half we look at will either contain the target or not

Time complexity
- best O(1), target = arr[mid] first time
- worst O(log n), target is not in arr so we break up problem log n times and binary search them all
- avg O(log n)

Space complexity
- O(1), doesn't need any more space?

Does it always pick up the first occurance of an element. No as in [1,1,1] searching for 1 will pick up the middle 1
"""

count = 0

def binary_search(arr, target):

    global count
    count += 1
    print(count)

    if len(arr) < 1:
        print("Not found")
        return -1
    mid = len(arr)//2
    if arr[mid] == target:
        print(str(target) + " found")
        return mid
    else:
        if target < arr[mid]:
            binary_search(arr[:mid], target)
        elif target > arr[mid]:
            binary_search(arr[mid+1:], target)

if __name__ == "__main__":
    arr = [1,2,3,4,4,4,5,6,7,8,9]
    binary_search(arr,11)