# Sorting

## Basic comparison based sorts

### Selection sort

Key idea:
1. starting from the 0th element
2. pick out the smallest element in the array
3. swap that with the current element
4. repeat for length of array - 1

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

| Situation   |   Time  | Space |
| ----------- | ------- | ---- |
| Best Case   | O(n^2)  | O(1) |
| Worst case  | O(n^2)  | O(1) |

Does not take into account if the array is already sorted so will result in looping O(n) and O(n) find mins, no extra base used.

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

| Situation   |   Time  | Space |
| ----------- | ------- | ---- |
| Best Case   | O(n)    | O(1) |
| Worst case  | O(n^2)  | O(1) |

If the array is already sorted and nothing needs to be placed then it is O(n) so you never enter the while loop. In the worst case you will loop over the array O(n) and place each element int the sorted portion which can be at most O(n).

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

Merge sort is table as the comparison is left ot right only taking the element from the right array if it is < than the element in the left array.

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

The reassurance relation in the worst case is looks like the arithmetic series where the time needed at level 0 is `cn`, time at level 1 is `c(n - 1)` and the time at level is is `c(n - i)` which sums to `c((n+1)(n/2)-1)` which is upper bounded by n^2. In the expected case where around half of the problem is truncated at each step it looks like that of merge sort.

Quick sort is not stable, consider:
```
array = [b, a, B, A], where a = A < b = b
say that b is chosen as the pivot.
the array will be rearranged as: A, a, B, b
in the paritioning loop
- A < b so it will swap with itself and wall will be incremented to 1
- a < b so it will swap with itself and wall will be incremented to 2
- B = b so nothing will happen
Then swap the last index (pivot) with wall resutling in [A, a, b, B].
The releative positioning of A and a has changed thus not stable.
```

### Heap sort

Key idea:
1. make use of the heap data structure (a.k.a priority queue) so you can put stuff in and take stuff out in sorted order.
2. heapify the input array (O(n log n) naively, O(n) smartly).
3. take n items out to form your sorted array O(n log n), every time you take an item out log n to fix the heap, take n items.

Note: Heaps can be represented as an array in implementation and visually as a tree.

#### Heapify

Naive O(n log n) vs better O(n).

Naively you can make a heap and insert each item. After insertion of an item it is O(log n) to maintain the heap property (percolate/sink down) so inserting n items results in O(n log n).

A better approach is to take advantage of leaves being valid sub heaps. Only sink down the nodes that we need to.

We don't need to deal with leaves so given the input array with length n we only care about the first 1 .. n // 2 nodes as the last n // 2 .. n nodes are most likely leaves.
So we only need to sink down the the first 1 .. n // 2 elements.  We need to do this smartly as if we start at index 1 (the root) it will assume sub heaps encountered uphold the heap property,
thus we must start from n // 2 and go up to 1 to ensure all sub heaps are fixed before fixing sub heaps from a higher level.

This works as leaves are valid heaps, because they are filled out from left to right we can kinda ignore the last n // 2 elements as they are
all leaves. So we then get the parents of these sub heaps and make sure they upload the heap property and do this from n // 2 until the root.

A complete binary tree with height h (root has h = 0) has at max (n + 1)//2 leaves, where n is the number of nodes and 2^(h + 1) -1 nodes.

```python
def heap_sort():
    heap.heapify(array)
    output = []
    for _ in range(heap.count):
        output.append(heap.get_min())
```

See [from algorithms_datastructures.datastructures.min_heap](https://github.com/darvid7/pls-hire-me/blob/fb_prep/algorithms_datastructures/datastructures/min_heap.py)

| Situation   |   Time     | Space |
| ----------- | ---------- | ----- |
| Best Case   | O(n log n)  | O(1) |
| Worst case  | O(n log n)  | O(1) |

Time is bounded by the log n time to remove a single element done for n elements.
Space is inplace (don't need more space) except for that of the array (assume it is given). Heap sort is not stable, no guarantee of order of same values in a heap.


## Non comparison based sorts

### Counting sort

Key idea:
1. make buckets of all possible inputs in the range.
2. loop through items in the array, add the count to the correct bucket.
3. return bucket key * count.

We need to know the range for counting sort.

```python
def counting_sort_ints(array):
    max_val = max(array)
    min_val = min(array)
    counts = [0] * (max_val - min_val + 1)
    output = [0] * len(array)
    counts_offset = min_val
    for value in array:  # Count occurrences.
        index = value - counts_offset
        counts[index] += 1
    for i in range(1, len(counts)):  # Cumulative sum so can loop backwards.
        counts[i] += counts[i - 1]
    for i in range(len(array) - 1, -1, -1):  # Loop backwards over input array.
        index = counts[array[i] - counts_offset] - 1  # Find the index to copy the value to.
        output[index] = array[i]
        counts[array[i] - counts_offset] -= 1
    return output

def counting_sort_alphabet(string):  # Not stable, can work with string or array.
    counts = [0] * 26  # Assumed lower case alphabet.
    output = []
    for char in string:
        index = ord(char) - ord('a')  # 'a' is index 0.
        counts[index] += 1
    for i in range(len(counts)):  # O(k) = O(26) loop, inner loop will only execute O(n) times.
        # This will not preserve stability but is ok when just dealing with single chars.
        ascii_value = ord('a') + i
        for c in range(counts[i]): # The amount of times this happens sums to O(n).
            output.append(chr(ascii_value))
    return "".join(output)
```

| Situation   |   Time     | Space    |
| ----------- | ---------- | -------- |
| Best Case   | O(2n + k)  | O(k + n) |
| Worst case  | O(2n + k)  | O(k + n) |

Counting sort can be implemented stably and not stably. It will be stable if you calculate the cumulative sum of the indexes and then loop over the input array and find out where to place each item in the output array like in `counting_sort_ints()`, it can also be done un-stably like in `counting_sort_alphabet()`
The complexity is treated as O(n). It does two loops over the input size n one to count and one to find placement of inputs. Then a loop to calculate the cumulative sum based on the range of the input size.
If the range is small compared to the length of the input it is bounded by O(n), else O(k).
O(k) extra space for the count array and O(n) for the output array.


### Radix sort
