"""
@author: David Lei
@since: 23/08/2016
@modified: 

Given an array, find the maximum sum for any
    1. non contiguous sub array
    2. contiguous sub array
"""
arr = [-500, 100, 5, 7, -90, -14, 8 ,1]

def max_subarray_non_contiguous(arr):
    table = [0] * len(arr)
    table[0] = arr[0]

    for i in range(1, len(arr)):
        table[i] = max((table[i-1] + arr[i]), arr[i], table[i-1])

    return table[-1]

#print(max_subarray_non_contiguous(arr))

def max_subarray_contiguous(arr):
    table = [0] * len(arr)
    table[0] = arr[0]

    for i in range(1, len(arr)):
        table[i] = max((table[i-1] + arr[i]), arr[i])

    return max(table)

#print(max_subarray_contiguous(arr))