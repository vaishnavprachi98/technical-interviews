"""
@author: David Lei
@since: 19/09/2017

Top Down memoization implementation of getting the nth fibonacci number.
"""


def fib(n):
    if n == 0:
        return MEMO[0]
    if n == 1:
        return MEMO[1]
    if MEMO[n] > 0:
        return MEMO[n]
    MEMO[n] = fib(n - 1) + fib(n - 2)
    print("Added computation {0} + {1} = {2} to memoization table".format(MEMO[n - 1], MEMO[n - 2], MEMO[n]))
    return MEMO[n]

n = 14
MEMO = [-1 for _ in range(n + 1)]
MEMO[0] = 0
MEMO[1] = 1

print(fib(n))