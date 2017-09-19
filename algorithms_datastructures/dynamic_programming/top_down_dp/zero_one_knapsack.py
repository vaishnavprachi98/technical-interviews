"""
@author: David Lei
@since: 19/09/2017

Knapsack problem where you can either pick the item or not.
If you pick an item the value you can get is the value of the item and the value of items you can get with remaining capacity.

Note: Solution is slightly different to https://www.youtube.com/watch?v=149WSzQ4E1g&ab_channel=TusharRoy-CodingMadeSimple

Note how the recursive code is so much more cleaner than bottom up iterative approach.
"""


def kanpsack(item_index, capacity):
    if capacity == 0:
        return 0
    if item_index >= N:
        return 0
    if MEMO[item_index][capacity] != -1:
        return MEMO[item_index][capacity]

    value_taking_current_item = 0
    if capacity - ITEM_WEIGHTS[item_index] >= 0:  # Can try take current item.
        value_taking_current_item = kanpsack(item_index + 1, capacity - ITEM_WEIGHTS[item_index]) + ITEM_VALUES[item_index]
    value_not_taking_current_item = kanpsack(item_index + 1, capacity)

    max_value = max(value_taking_current_item, value_not_taking_current_item)
    MEMO[item_index][capacity] = max_value
    return max_value


if __name__ == "__main__":
    print("Scenario 1, expect 13")
    ITEM_WEIGHTS = [2, 2, 4, 5]
    ITEM_VALUES = [2, 4, 6, 9]
    TOTAL_CAPACITY = 8
    MEMO = [[-1 for _ in range(TOTAL_CAPACITY + 1)] for _ in range(len(ITEM_WEIGHTS))]
    N = len(ITEM_WEIGHTS)
    print(kanpsack(0, TOTAL_CAPACITY))

    print("Scenario 2, expect 9")
    ITEM_WEIGHTS = [1, 3, 4, 5]
    ITEM_VALUES = [1, 4, 5, 7]
    TOTAL_CAPACITY = 7
    MEMO = [[-1 for _ in range(TOTAL_CAPACITY + 1)] for _ in range(len(ITEM_WEIGHTS))]
    N = len(ITEM_WEIGHTS)
    print(kanpsack(0, TOTAL_CAPACITY))

    print("Scenario 3, expect 90")
    ITEM_WEIGHTS = [5, 4, 6, 3]
    ITEM_VALUES = [10, 40, 30, 50]
    TOTAL_CAPACITY = 10
    MEMO = [[-1 for _ in range(TOTAL_CAPACITY + 1)] for _ in range(len(ITEM_WEIGHTS))]
    N = len(ITEM_WEIGHTS)
    print(kanpsack(0, TOTAL_CAPACITY))

""" State tree

k = knapsack, k(n ,c)

Params for recursion:
    n = index of current item to consider
    c = capacity
Other variables used:
    v = value, local variable of taking/not taking an item at a recursive call
    v1 means take the item n
    v2 means don't take the item n
    r = return value
    r1 means the return value from taking item n
    r2 means the return value from not taking item
    M is the memoization table.
    N is the total number of items
total_capacity = 8

item index:     0  1  2  3
item_weights = [2, 2, 4, 5]
item_values =  [2, 4, 6, 9]

                                                    k(n=0, c=8) v=0 # Start state we are deciding to take item 0 or not, c = 8.
                                                    v1=2        v2=0
                                                    r1=10       r2=13
                                                    M[0][8] = max(v1+r1, v2+r2)
                                                    return 13 ______________________________________________________________________________________
                                                   /                                                                                                \
                                            take item 0                                                                                     don't take item 0
                                                 /                                                                                                    \
                                           k(n=1, c=6)                                                                                               k(n=1, c=8)
                                          v1=4               v2=0                                                                               v1=4            v2=0
                                          r1=6               r2=9                                                                               r1=9            r2=9
                                          M[1][6] = max(v1+r1, v2+r2)                                                                           M[1][8] = max(v1+r1, v2+r2)
                                       __ return 10                 \                                                                           return 13                  \
                                      /                              \                                                                          /                           \
                                     /                                \                                                                        /                             \
                               take item 1                          don't take item 1                                                   take item 1                        don't take item 1
                                   /                                    \                                                                   /                                  \
                              k(n=2, c=4)                               k(n=2, c=6)                                                     k(n=2, c=6)                           k(n=2, c=8)
                           v1=6          v2=0                           v1=4       v2=0                                                 repeated state                      v1=6         v2=0
                           r1=0          r2=0                           r1=0       r2= 9                                                already computed best               r1=0         r2=9
                           M[2][4] = max(v1+r1, v2+r2)                  M[2][6] = max(v1+r1, v2+r2)                                     value we can get with               M[2][8] = max(v1+r1, v2+r2)
                           return 6                                     return 9                                                        c=6 deciding to take                return 9________
                          /              \                               /              \                                               item at idx2. note that              /              \
                    take item 2          don't take item 2       take item 2      don't take item 2                                     we can only look at            take item 2      don't take item 2
                        /                   \                          /                  \                                             items after 2 if we                /                  \
                    k(n=3, c=0)            k(n=3, c=4)           k(n=3, c=2)            k(n=3, c=6)                                     continue the recursion.       k(n=3, c=4)               k(n=3, c=8)
                    return 0 as c=0        can't take item 3     can't take item 3      v1=9    v2=0                                    return M[2][6]                repeated state.       v1=9         v2=0
                    M[3][0] = 0            as weight[n] > c      as weight[n] > c       r1=0     r2=0                                                                 weight[3] > c.        r1=0         r2=0
                                           can't try next item   can't try next item    M[3][6] = max(v1+r1, v2+r2)                                                   return M[3][4]        M[3][8] = max(v1+r1, v2+r2)
                                           as n+1 > N            as n+1 > N             return 9                                                                                            return 9______
                                           M[3][4] = 0           M[3][c] = 0            /              \                                                                                    /             \
                                           return 0              return 0           take item 3     don't take item 3                                                                    take item 3    don't take item 3
                                                                                      /                  \                                                                                /                 \
                                                                                k(n=4,c=1)             k(n=4, c=6)                                                                    k(n=4, c=3)          k(n=4, c=8)
                                                                                N out of bounds        N out of bounds                                                                n + 1 > N            n + 1 > N
                                                                                return 0               return 0                                                                       return 0             return 0

From the state tree we can see the optimal solution is 13 done by not taking item 0, taking item 1, not taking item 2 and taking item 3.
We can see how we avoid recomputing a lot of information by using our memoization table.

Also note that in the bottom up tabulation solution the entire table will be filled out O(total_capacity *  num_items), in this case not every state in that table is visited.
For example we will never have the state n=1, c=1 as we can't make that by subtracting any combination of weights from capacity, this means not every state is explored, just every possible state.

This solution makes a lot of sense, looking at state k(n=3, c=8) we can see that as n=3 we can only take the last item with weight 5.
There are only two possible out comes, take it or not.
We don't care about how we got to this state nor what we took in the past nor if we have enough capacity to visit other items earlier in our array (they should be computed earlier in the recursive calls).
It is purely dependent on the current state and what we can do from here.
"""