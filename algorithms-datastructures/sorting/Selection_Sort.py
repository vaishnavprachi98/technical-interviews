"""
@author: David Lei
@since: 21/08/2016
@modified:

How it works: select the minimum item in the list, move that to the position we are up to and keep going
Invariants: as we move through array, left most to where we are now is sorted

Time complexity
- best O(n^2), out loops once, inner will always still try and find the min value which is O(n)
- worst O(n^2)
- avg O(n^2)

Space complexity
- O(1), doesn't need any more space

Stability: no due to the swapping
    b c B a A
    if a = A < B = b < c
    first iteration will result in: a c B b A
    second iteration will result in: a A B b c
    this is sorted
    relative posotion of b and B went from b B to B b, so not stable
"""

def selection_sort(arr):
    count = 0
    for i in range(len(arr)-1): # only need to loop n-1 items as last item won't be selected as min as it is max
        min_idx = i
        min_so_far = arr[i]
        count += 1
        # find min
        for j in range(i, len(arr)): # loop up to until end to find min
            if arr[j] < min_so_far:
                min_idx = j
                min_so_far = arr[j]
            count += 1
        # swap where we are up to and the min
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(count)
    return arr

if __name__ == "__main___":
    arr = [1,2,3,4,5,6,7,8]
    print(selection_sort(arr[::-1]))

    # sorted already, still count = 42
    # reverse sorted, count = 42