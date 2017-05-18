"""
@author: David Lei
@since: 18/05/2017
@modified: 

http://www.geeksforgeeks.org/find-the-maximum-repeating-number-in-ok-time/

Restrictions: O(n) time, O(1) space.

Given array of integers, print integer that occurs the most.
"""


def max_repeating_number(arr):
    k = max(arr) + 1
    for i in range(len(arr)):
        arr[arr[i] % k] += k
    print(arr)
    max_value = max(arr)
    print(arr.index(max_value))


"""  Why does this work?

Looping through array indices: 0 8

i = 0:
    arr[2 % 8] += 8 => arr[2] += 8
    [2, 3, 11, 5, 3, 4, 1, 7]
     x      ^
i = 1:
    arr[3 % 8] += 8 => arr[3] += 8
    [2, 3, 11, 13, 3, 4, 1, 7]
        x       ^
i = 2:
    arr[11 % 8] += 8 => arr[3] += 8
    [2, 3, 11, 21, 3, 4, 1, 7]
            x   ^
i = 3:
    arr[21 % 8] += 8 => arr[5] += 8
    [2, 3, 11, 21, 3, 12, 1, 7]
                x       ^
i = 4:
    arr[3 % 8] += 8 => arr[3] += 8
    [2, 3, 11, 29, 3, 12, 1, 7]
                ^  x
i = 5:
    arr[12 % 8] += 8 => arr[4] += 8
    [2, 3, 11, 29, 11, 12, 1, 7]
                    ^  x
i = 6:
    arr[1 % 8] += 8 => arr[1] += 8
    [2, 11, 11, 29, 11, 12, 1, 7]
        ^                   x
i = 7:
    arr[7 % 8] += 8 => arr[7] += 8
    [2, 11, 11, 29, 11, 12, 1, 15]
                               ^x
Note: Every time a 3 in the original array is processed (that index), the value at index 3 is incremented.

The index of the maximum value is the maximum repeating element. arr[3] = 29 = max, max repeating element = 3.
"""

arr = [2, 3, 3, 5, 3, 4, 1, 7]
max_repeating_number(arr)
