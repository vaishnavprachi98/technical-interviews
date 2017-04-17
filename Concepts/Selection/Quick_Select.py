"""
@author: David Lei
@since: 28/08/2016
@modified: 

Worst: O(n^2)
Best: O(n)

to find 3rd smallest element in array, a = [5, 4, 1, 2, 9, 8, 6]
    split array into 2 around a pivot, eg: make pivot 6
        less than 6 = [5, 4, 1, 2]
        greater than 6 = [6, 8]

        len(less than) = 4
        2 < 4 so do again
            pivot = 2
            less than = [1]
            greater than = [4, 5]

            len(less than) = 1, len(greater than) = 2

# given unsorted array, find kth smallest element
# same as sorting and finding item at index k
# but can do without complete sorting the entire array
"""
import random
def randomized_partition(array, start, end):
    random_index = random.randint(start, end)
    array[random_index], array[end] = array[end], array[random_index]
    # picked pivot 'randomly', put it at the end index
    # now partition
    pivot = array[end]          # randomly chosen pivot
    wall = start - 1
    for i in range(start, end):
        if array[i] <= pivot:
            wall += 1           # wall is <= pivot
            array[i], array[wall] = array[wall], array[i]       # swap elements
    array[wall + 1], array[end] = array[end], array[wall + 1]   # put pivot in right place
    return wall + 1             # index of pivot


def randomized_quick_select(array, start, end, i):
    """
    returns ith smallest element in an array[start...end]
    :param array: array of distinct elements
    :param start: start index to look at
    :param end: end index to look at
    :param i: something th smallest index we want
    """
    if start == end:                    # base case
        return array[start]
    pivot_index = randomized_partition(array, start, end)
    k = pivot_index - start + 1
    if i == k:
        return array[pivot_index]
    elif i < k:
        return randomized_quick_select(array, start, pivot_index-1, i)      # recurse on lower half
    else:
        return randomized_quick_select(array, pivot_index+1, end, i-k)      # recurse on upper half

if __name__ == "__main__":
    a = [1,2,3,4,5,6,8]
    print(randomized_quick_select(a[::-1], 0, 6, 1))