"""
@author: David Lei
@since: 7/11/2017

https://www.hackerrank.com/challenges/qheap1/problem

Passed :)
"""

import heapq

n = int(input())

heap = []

MAX_VALUE = 10 ** 9 + 1

values_to_delete = {}

for _ in range(n):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        # Add value.
        heapq.heappush(heap, query[1])
    elif query[0] == 2:
        # 'Delete' this value.
        # instead of a linear search just node that we want to delete this value and
        # if we ever print it as the min we can remove it then.
        # This gets rid of the TLE :D
        if query[1] in values_to_delete:
            values_to_delete[query[1]] += 1
        else:
            values_to_delete[query[1]] = 1
        # # Delete element v from the heap.
        # heap.remove(query[1]) # Remove first occurrence of query[1]
        # heapq.heapify(heap) # Time lim if I heapify O(n).
        # # I want a min so put in max value.
    else:
        min_val = heap[0]
        # At worst need to do O(n) removes of log n time.
        # Which is better than a O(n) search, O(n) heapify for O(n) deletions.
        while min_val in values_to_delete and values_to_delete[min_val] >= 1:
            values_to_delete[min_val] -= 1
            heapq.heappop(heap)
            min_val = heap[0]

        print(min_val)