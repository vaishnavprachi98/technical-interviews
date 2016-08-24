"""
@author: David Lei
@since: 21/08/2016
@modified:

How it works: at each stage, divide the problem around a pivot into 2 partitions. One containing things less than the
                pivot and another containing things greater or eqal to the pivot. Note that the paritioned lists will not
                include the pivot. This will keep on going until the list is of len 1 and then we can just put the overall
                list back together.

Invariants: section < pivot | pivot | section >= pivot

Compared to merge: work is done in the splitting of the array

Time complexity
- best O(n log n), when a decent pviot is chose for around event splitting
- worst O(n^2), when the pviot only discards one element from the array each time, thus needs to do it N^2 times
- avg O(n log n)

Space complexity - can do O(log n) note? figure out how
- O(N), create new lists when we split, for partitionaing arrays
- O(log n), when in place, still need log n space to for recursive calls to stall stack frames

I understand that both quick sort and merge sort need O(n) auxiliary space for the temporary sub-arrays that
are constructed, and in-place quick sort requires O(log n) auxiliary space for the recursive stack frames.
http://stackoverflow.com/questions/22233532/why-does-heap-sort-have-a-space-complexity-of-o1

There is a more complex version which uses an in-place partition algorithm and can achieve the complete sort
using O(log n) space (not counting the input) on average (for the call stack).
http://stackoverflow.com/questions/12573330/why-does-quicksort-use-ologn-extra-space

Stability: Not stable
"""
count = 0

def quick_sort(arr):
    """
    This works and uses the idea of quick sort but it can be done in place of the one array instead of making a new
    array which takes space
    """
    global count
    count += 1
    print(count)

    if len(arr) <= 1:
        return arr
    else:
        ### PARTITION ARR
        # assume last item chosen as pivot
        pivot = arr[-1]

        wall = 0                        # everything before wall is < pivot
        for i in range(len(arr)-1):     # last element is pivot
            if arr[i] < pivot:
                temp = arr[wall]        # less than pivot
                arr[wall] = arr[i]      # move to index wall (everything before it will be <)
                arr[i] = temp
                wall += 1               # increment wall (so arr[i] is < pivot, now it is behind the wall)
        arr[len(arr)-1] = arr[wall]     # swap pivot with first element !< pivot
        arr[wall] = pivot

        less_than = quick_sort(arr[:wall])
        greater_eq_than = quick_sort(arr[wall+1:])

        return less_than + arr[wall:wall+1] + greater_eq_than

# more pythonic solution
# http://stackoverflow.com/questions/25690175/bucket-sort-faster-than-quicksort

pythonic_count = 0
def pythonic_quick_sort(arr):         # more pythonic
    global pythonic_count
    pythonic_count += 1
    print(pythonic_count)
    if len(arr) <= 1:
        return arr
    low, pivot, high = partition(arr)
    return quick_sort(low) + [pivot] + quick_sort(high)     # note [1] or [pivot] is a list of len 1


def partition(arr):
    pivot = arr[-1]
    # inefficient space of merge sort
    low = [arr[x] for x in range(len(arr)-1) if arr[x] < pivot]
    high = [arr[x ]for x in range(len(arr)-1) if arr[x] >= pivot]
    return low, pivot, high


def quick_sort_inplace(arr, low, hi):
    #low = 0
    #hi = len(arr)

    if (hi-low) <= 1:           # array of len 1 eg first index, low = 0, hi = 1
        return                  # array[start:to_non_inclusive]

    else:
        l_start, l_end, pivot_idx, ge_start, ge_end = partition_inplace(arr, low, hi)
        quick_sort_inplace(arr, l_start, l_end)
        quick_sort_inplace(arr, ge_start, ge_end)

        return arr

def partition_inplace(arr, low, hi):
    """
    low = start index of this sub array to partition
    hi = end index + 1 of this sub array to partition

    inplace (using the same array)
    restrict the array with the bounds arr[low:hi]
        1. make pivot the last element of the section we are looking at
        2. make some pointers to keep track of the part that is lower than pivot and greater than pivot
        3. loop over array from low to hi inclusive
        4. if element is < swap it with the first element that is greater (element at index wall)

    invariant: everything before wall is < pivot, everything after wall that we have already looked at is >= pivot
    """
    pivot = arr[hi-1]                                  # take pivot to be the last element
    wall = low                                      # everything before the is < pivot
    for i in range(low, hi, 1):                     # loop from low to hi inclusive
        if arr[i] < pivot:                          # if less than pivot swap element at wall with the less than element
            arr[wall], arr[i] = arr[i], arr[wall]
            wall += 1
    arr[hi-1] = arr[wall]                           # put pivot in the right place
    arr[wall] = pivot
    # array mutated, don't need to return it
    # low = start of section < pivot
    # wall-1 = end of section < pivot
    # wall = pivot
    # wall+1 = start of section >= pivot
    # hi = end of section >= pivot
    return low, wall, wall, wall+1, hi



if __name__ == "__main__":
    arr = [1,2,3,4]
    bar = [8, 100 ,1,-3,11,1,0]
    car = [0,-3,1,-2]
    foo = [123,91,-19, 1,1,2,1,-54,1909,-51293,192,3,-4]
    #print(quick_sort(foo))
    #print("\nPythonic version\n")
    #print(pythonic_quick_sort(foo))
    print("\nInplace version\n")

    print(quick_sort_inplace(foo, 0, len(foo)))