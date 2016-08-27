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

def houses_hate_neighbours_proper(arr, k):
    # initalize table
    table = [0] * len(arr)
    table[0] = arr[0]
    for i in range(1, len(arr)):    # chuck in the best so far for your base cases
        if i < k + 1:
            table[i] = max(table[i-1], arr[i])
        else:
            table[i] = max(table[i-k-1] + arr[i], table[i-1])   # look back on the best so far value -k-1 places
    best = max(table)
    # find solution
    partial_soln = best
    solution = []
    was_equal = False
    for j in range(len(table)-1, -1, -1):
        if table[j] == partial_soln:
            was_equal = True
            if j == 0:
                partial_soln -= arr[j]
                solution.append(arr[j])
            else:
                pass
        else:
            if was_equal:
                partial_soln -= arr[j + 1]
                solution.append(arr[j + 1])
                was_equal = False
    print(partial_soln)
    print("Solution: " + str(solution))
    print("Max val: " + str(best))

    print(table)

    # left most occurrence of maximum



def houses_hate_neighbours(arr, k):

    can_grab = len(arr)//k

    table = [0]*len(arr)                  # make dp table

    for j in range(k+1):                  # add first k+1 values to the dp table
        table[j] = arr[j]                 # as from index 0 we need to skip k so the first k+1 elements will be the same as in arr

    for i in range(k+1, len(arr)):        # loop for the rest of the array

        check_idx = i - k - 1             # check index is the index we look at
        """
        example explanation: for k = 3
        index 4 which has the value 40 can look at index 0 (4-k-1) which has the value 50 and take the sum as you must
        skip at least k houses
        however at index 5 which has the value 95 we can look at index 1 (5-k-1) and take the sum which is 105
        but this is not optimal as we should also consider looking at index 0 (5-k-2) which will give us 145 which
        leads to the optimal solution

        can_grab is the max number of previous indexes we should consider which is given by len(arr)//k
        for an array of length 10 and k of 3, we should at max consider the following indexes when looping through to
        find a solution. At index j check:
                index j - k - 1     has an 'offset' of 0 so, index j - k - 1 - 0
                index j - k - 2     has an 'offset' of 1 so, index j - k - 1 - 1
                index j - k - 3     has an 'offset' of 2 so, index j - k - 1 - 2
        assuming we stay inside the bounds of the array

        this way we can find the max possible value with skipping at least k houses

        offset <= can_grab
        """
        offset = 0
        for x in range(can_grab, -1, -1):   # find the max offset, will loop for len(arr)//k times
            if check_idx - x >= 0:
                offset = x
                break

        max_val = arr[i] + table[check_idx]                  # assume with offset 0, we have the largest value
        for c in range(1,offset+1):                          # check all things from offset to check with cur number
            check_this = table[check_idx - offset] + arr[i]
            if check_this > max_val:
                max_val = check_this

        table[i] = max_val                                   # add the largest value into the dp table

    print(arr)
    print(table)
    return max(table)
if __name__ == "__main__":

    print(houses_hate_neighbours_proper([50, 10, 12, 65, 40, 95, 100, 12, 20, 30], 3))
