# Sorting

## Basic comparison based sorts

### Selection sort

Key idea:
1. starting from the 0th element
2. pick out the smallest element in the array
3. swap that with the current element
4. repeat for length of array - 1

| Situation   |   Time  | Space |
| ----------- | ------- | ---- |
| Best Case   | O(n^2)  | O(1) |
| Worst case  | O(n^2)  | O(1) |

Does not take into account if the array is already sorted so will result in looping O(n) and O(n) find mins, no extra base used.

```python
def selection_sort(array):
    for j in range(len(array) - 1):  # For each element index.
        min_i = j
        for k in range(j, len(array)):  # For element indexes in range start until end.
            if array[k] < array[min_i]:
               min_i = k
        array[j], array[min_i] = array[min_i], array[j]
    return array
```

Note: This is note a stable sort, consider:
```
array = b c B a A where a = A < B = b < c
 - first iteration will result in: a c B b A
 - second iteration will result in: a A B b c
 - this is now sorted
relative position of b and B went from b B to B b, so not stable
```
### Insertion sort

Key idea:
1. starting from the 0th element assume that is sorted
2. extend the sorted component by 1, pick out the next element and put it into the sorted component.
4. repeat for length of array - 1

| Situation   |   Time  | Space |
| ----------- | ------- | ---- |
| Best Case   | O(n)    | O(1) |
| Worst case  | O(n^2)  | O(1) |

If the array is already sorted and nothing needs to be placed then it is O(n) so you never enter the while loop. In the worst case you will loop over the array O(n) and place each element int the sorted portion which can be at most O(n).


```python
def insertion_sort(array):
    for j in range(1, len(array)):  # For each element index.
        index = j
        value = array[j]
        while index > 0 and value < array[index - 1]:
            array[index] = array[index - 1]  # Copy over.
            index -= 1  # Careful, should only decrement after the copy.
        array[index] = value
    return array
```

## Better comparison based sorts

### Merge sort

Key idea:
1. divide problem set into half via recursion.
2. solve the base case, an array of length 1 is sorted.
3. merge up arrays as recursive calls return
4. the resulting merged array is sorted.

```python

def merge_arrays(left, right):
    result = [0 for _ in range(len(left) + len(right))]
    result_index = 0
    left_index = 0
    right_index = 0
    while True:
        if left_index >= len(left):
            # Copy over rest of right.
            for i in range(right_index, len(right)):
                result[result_index] = right[i]
                result_index += 1
            break
        if right_index >= len(right):
            # Copy over rest of left.
            for i in range(left_index, len(left)):
                result[result_index] = left[i]
                result_index += 1
            break
        if left[left_index] <= right[right_index]:
            result[result_index] = left[left_index]
            result_index += 1
            left_index += 1
        else:  # right is < left.
            result[result_index] = right[right_index]
            result_index += 1
            right_index += 1
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge_arrays(left, right)
```

| Situation   |   Time      | Space |
| ----------- | ----------- | ---- |
| Best Case   | O(n log n)  | O(n) |
| Worst case  | O(n log n)  | O(n) |

Merge sort splits up the problem size by a factor of 2 each time resulting log n recursive calls. The complexity for merging is upper bounded by O(n) space and O(n) time as you need an auxiliary array and to iterate through n items.
Each recursive call requires a merge and it is upper bounded by the O(n) merge. So with log n splits requiring n to merge conceptually you can see how merge sort is O(n log n).

The reassurance of merge sort is `T(n) = 2T(n/2) + n` which can be used to show the O(log n) time complexity.

Merge sort applies divide and conquer because cutting the problem up into smaller pieces (dividing) and then putting the problem back together (conquering).

### Quick sort

Key idea:
1. pick a pivot.
2. sort array elements around the pivot such that elements on the left <= pivot < elements on the right.
3. swap pivot with wall, this is so you get the pivot in the middle and the left half is <= and the right half is >.
4. call quick sort on each partition not including the pivot.
5. merge results as recursive calls return.

```python
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = len(array) // 2  # Assume mid point as pivot.
    wall = 0  # Everything before the wall will be lower than array[pivot].
    for i in range(len(array)):  # This partitions the array such that elements less than pivot < wall <= elements greater equal to pivot.
        if array[i] < array[pivot]:
            array[i], array[wall] = array[wall], array[i]
            wall += 1
    pivot_element = array[pivot]
    array[pivot], array[wall] = array[wall], array[pivot]
    left = quick_sort(array[:wall])  # Up until pivot not inclusive.
    right = quick_sort(array[wall + 1:])  # From pivot + 1 inclusive to the end.
    return left + [pivot_element] + right
```

| Situation   |   Time      | Space |
| ----------- | ----------- | ---- |
| Best Case   | O(n log n)  | O(n) |
| Worst case  | O(n^2)      | O(n) |

Note: The O(n) space is for the naive implementation where we store the left and right arrays bounded by O(n), a better implementation can get O(log n) space.

The best case is n log n assuming that the problem space is divided equally. The worst case is when only 1 element is removed from the problem set at each time leading to the recursion tree looking like a linear chain.
In each call we loop through the n items in that call comparing it to the pivot, this in the worst case becomes an O(n) loop thus the worst case time complexity is O(n^2). In the best and expected case the problem set is divided by a log factor, and a O(n) loop to partition is needed which hints at the O(n log n) complexity, O(log n) partitions, each partition takes O(n) operations.

The reassurance relation in the worst case is looks like the arithmetic series where the time needed at level 0 is `cn``, time at level 1 is `c(n - 1)` and the time at level is is `c(n - i)` which sums to `c((n+1)(n/2)-1)` which is upper bounded by n^2. In the expected case where around half of the problem is truncated at each step it looks like that of merge sort.



## Non comparison based sorts

### Counting sort

### Radix sort