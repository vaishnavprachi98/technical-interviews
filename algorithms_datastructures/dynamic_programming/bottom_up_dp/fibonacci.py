"""
@author: David Lei
@since: 19/09/2017

Bottom up solution to find the nth fibonacci number.
"""


def fib(n):
    TABLE = [0, 1]
    calculated = 1

    while calculated < n:
        next_number = TABLE[calculated] + TABLE[calculated - 1]
        print("Adding computed value to table {0} + {1} = {2}".format(
            TABLE[calculated ], TABLE[calculated - 1], next_number))
        TABLE.append(next_number)
        calculated += 1
    return TABLE[n]

print(fib(14))
