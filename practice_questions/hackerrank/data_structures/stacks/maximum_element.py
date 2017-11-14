"""
@author: David Lei
@since: 7/11/2017

https://www.hackerrank.com/challenges/maximum-element/problem

Instead of doing this naively we try it with getting the max in O(1) time instead of O(n) searching through the stack.

LOL can do this easily storing the value and the max value.

Passed :)
"""
queries = int(input())

stack = [] # Holds (value, max_value) pair.
max_value = 0
for _ in range(queries):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        max_value = max(max_value, query[1])
        stack.append((query[1], max_value))
    elif query[0] == 2:
        stack_node = stack.pop()
        if stack_node[1] == max_value:
            # Need to reset max value
            if stack:
                max_value = stack[-1][1] # Next max
            else:
                max_value = 0
    else:
        print(stack[-1][1])
