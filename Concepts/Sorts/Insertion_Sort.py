"""
@author: David Lei
@since: 21/08/2016
@modified: 

How it works: assume the first item is sorted (very left of arr), take the next unsorted item and put it in the correct
              position of the sorted portion
              loop once on array, loop a number of times on sorted portion
Invariants: left part is always sorted

Outerloop always N
Inner depends on number of swaps
avg case: http://stackoverflow.com/questions/17055341/why-is-insertion-sort-%CE%98n2-in-the-average-case

Time complexity
- best O(n), when list is already sorted
- worst O(n^2), when list is sorted in reverse
- avg O(n^2)

Space complexity
- O(1), doesn't need any more space

Stability: yes as only sawp if > and not >=
"""

def insertion_sort(arr):
    count = 0                       # loop (1, len(arr)) remember looping to len(arr) will loop for the length of the array
    for i in range(1, len(arr)):    # assume first element is sorted, loop until the end of the array
        idx = i-1                   # this is the start of the sorted porition
        temp = arr[i]               # first unsorted element
        count += 1
        while idx >= 0 and arr[idx] > temp: # check temp (where we are up to in outer loop) against sorted position
            arr[idx+1] = arr[idx]           # copy bigger item in sorted portion into next index to the right
            idx -= 1                        # reduce idx to look at next item in sorted portion
            count += 1
        arr[idx+1] = temp           # copy temp into the correct position
    print(count)
    return arr

if __name__ == "__main___":
    arr = [1,2,3,4,5,6]
    print(insertion_sort(arr[::-1]))




