# Selection

## Quick Select

Key idea:
- find the kth smallest element in an array
- partition around the kth element

Partitioning (same as quicksort):
1. pull out pivot element (swap with last element)
2. put smaller elements on the left
3. put larger elements on the right (don't actually need to do this)
4. replace pivot element

Select:
1. guess where the kth smallest element is (kinda does a binary search)
2. take a guess and pick an element
3. check your guess via partitioning
4. if it ends up in the right place you are done.
5. if you are wrong do the same in one half of the partition.

```python
def quick_select_partition(array, start, end, pivot_index):  # Inplace.
    array[end], array[pivot_index] = array[pivot_index], array[end]
    pivot_element = array[end]
    wall = start # Things left to the wall are smaller, right are bigger.
    for i in range(start, end):  # Exclusive of end as the pivot is now there.
        if array[i] < pivot_element:
            array[i], array[wall] = array[wall], array[i]
            wall += 1
    array[end], array[wall] = array[wall], array[end]
    return wall  # Will no return 0 but will return the value starting at start.

def quick_select(array, start, end, k):
    if start == end: # Only 1 element, return it.
        return array[start]
    pivot_index = (start + end) // 2
    pivot_index = quick_select_partition(array, start, end, pivot_index)  # Returns true position of pivot.
    k_smallest_element_index = k -1
    if k_smallest_element_index == pivot_index:  # We look for the kth smallest so the kth smallest is at index k.
        return array[k_smallest_element_index]
    elif k_smallest_element_index < pivot_index: # kth smallest element is in the bottom half.
        return quick_select(array, start, pivot_index - 1, k)
    else:                 # kth smallest element is in the top half.
        return quick_select(array, pivot_index + 1, end, k)
```

| Situation   |   Time  | Space |
| ----------- | ------- | ---- |
| Best Case   | O(n)    | O(1) |
| Worst case  | O(n^2)  | O(1) |

An alternate approach is to sort which is `O(n log n)` then find the kth smallest element at the `kth` index.

Quickselect is an alternate method which has best case `O(n)`

## Median of medians thingy