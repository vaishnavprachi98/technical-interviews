"""
@author: David Lei
@since: 19/10/2017

Mostly works for https://www.hackerrank.com/challenges/longest-increasing-subsequent/problem
Except for TLE because an n log n solution exists.

Works on leetcode https://leetcode.com/problems/longest-increasing-subsequence/description/
"""

def longest_increasing_subsequence(array):
    table = [1] * len(array)
    aux = [i for i in range(len(array))]
    for i in range(1, len(array)):  # O(n^2)
        for j in range(0, i):
            if array[j] < array[i]:  # Can increment lis.
                if table[i] > table[j]:  # table[i] has a longer lis which doesn't include arr[j], don't do anything.
                    continue
                table[i] = table[j] + 1  # Add 1 to represent taking arr[j].
                aux[i] = j
    # Find the lis and the ending index of the lis.
    max_lis = max(table)  # Max lis not always at last element.
    lis_index = table.index(max_lis)  # These operations are probs O(n).
    lis = []
    while True:  # O(n) Find the actual lis using the aux array.
        lis.append(array[lis_index])
        lis_index = aux[lis_index]
        if table[lis_index] == 1:
            break
    lis.append(array[lis_index])
    return lis[::-1]

def hackerrank_test():
    arr = [29471, 5242, 21175, 28931, 2889, 7275, 19159, 21773, 1325, 6901]
    print(longest_increasing_subsequence(arr))

if __name__ == "__main__":
    arr = [3, 4, -1, 0, 6, 2, 3]
    lis = longest_increasing_subsequence(arr)
    print(lis)

    arr2 = [2, 7, 4, 3, 8]
    print(longest_increasing_subsequence(arr2))

    arr3 = [15, 27, 14, 38, 26, 55, 46, 65, 85]
    print(longest_increasing_subsequence(arr3))

    hackerrank_test()