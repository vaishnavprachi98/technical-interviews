"""
@author: David Lei
@since: 19/09/2017

https://www.youtube.com/watch?v=Kf_M7RdHr1M&ab_channel=TusharRoy-CodingMadeSimple

Top down recursive implementation of minimum number of coins to make value problem.
"""
# Can test on:
# coins = [9, 6, 5, 1], t = 11, ans = 2
# coins = [25, 10, 5], t = 30, ans = 2

coins = [1, 2, 3, 100, 156]
value = 8

# Note: Usually better to use tables in competitive programming, will stress dicts/maps to worst case performance.
# C++ maps implemented with R/B Tree O(log n) worst case.
# Python dicts implemented with hash table O(n) worst case.

MEMO = {}  # Map value: min number of coins to form it, can use a value * len coins table instead (tabulation) or a array of value.
MEMO_ARR = [-1 for _ in range(value + 1)]

# O(value * len(coins)), if no memoization will be exponential.
def min_coins(value):
    if value == 0:  # Base case, 0 coins to make value 0.
        return 0
    if MEMO_ARR[value] >= 0:
        return MEMO_ARR[value]
    # if value in MEMO:
    #     return MEMO[value]
    min_coins = None
    for coin in coins:
        if coin > value:
            continue
        return_value = min_coins(value - coin)
        # Add 1 to show we have taken 1 coin (the coin chosen in the current iteration of the for loop).
        min_coins = return_value + 1 if not min_coins else min(min_coins, return_value + 1)
    # MEMO[value] = min_coins
    MEMO_ARR[value] = min_coins
    print("Added value {0} to map, can be made using {1} coins".format(value, min_coins))
    return min_coins

print(min_coins(value))

""" State space to consider:

value = 5
coins = [1, 2, 3]

Recursive tree:
                                    5
                                 1, 2, 3

                              / pick first coin, subtract value from total

                            4
                         1, 2, 3

                        / pick coin 1, subtract value from total.

                      3
                   1, 2, 3

                 / pick coin 1, subtract value from total.

                2
             1, 2, 3

            / pick coin 1, subtract value from total.

           1
        1, 2, 3

      / pick coin 1, subtract value from total, upon first return takes 0 coins so we know it takes us 1 coin to form 1 as it was previously selected before calling rec(0)
      |  then pick coin 2, it is > 1 so it can help form 1, likewise with 3 then return the min.
     /

    0
  1, 2, 3
  0 coins to make value 0, return 0.

We try every coin by picking the coin to look at and subtracting the value from the total.
This gives us the smaller problem how many coins do I need to make a value less than the total by using a previously selected coin.
"""