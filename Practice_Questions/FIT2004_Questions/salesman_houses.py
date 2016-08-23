"""
@author: David Lei
@since: 23/08/2016
@modified: 

FIT2004 practice problem

given an
- array of houses (integers)
- k, an integer
each house doesn't like the k houses on ether side of it
what is the maximum value
k = 3 maent to be 175

      0   1   2   3
init: 50, 10, 12, 65
        40 (idx = 4) can look at 50
        95 (idx = 5) can look at 10, 50
        105 (idx = 6) can look at 12, 10, 50

        112 (idx = 7) can look at 65, 12, 10, 50
"""

def houses_hate_neighbours(arr, k):

    can_grab = len(arr)//k

    table = [0]*len(arr)                  # make dp table

    for j in range(k+1):                  # add first k values to the dp table
        table[j] = arr[j]

    for i in range(k+1, len(arr)):

        check_idx = i - k - 1

        offset = 0
        for x in range(can_grab, -1, -1):
            if check_idx - x >= 0:
                offset = x
                break

        max_val = arr[i] + table[check_idx]
        for c in range(1,offset+1):     # check all things from offset to check with cur number
            check_this = table[check_idx - offset] + arr[i]
            if check_this > max_val:
                max_val = check_this


        table[i] = max_val

    print(arr)
    print(table)
    return max(table)
print(houses_hate_neighbours([50, 10, 12, 65, 40, 95, 100, 12, 20, 30], 3))
