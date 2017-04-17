"""
@author: David Lei
@since: 21/08/2016
@modified: 

Common problem with many variations
    - minimum number of coins
    - how many ways can we give change
        - each coin only used once
        - each coin can be used as many times as you want
    etc
"""

"""
Minimum number of coins variation
Given coins of different denomination how many minimum coins are needed to get our desired total assuming
an unlimited supply of coins

https://www.youtube.com/watch?v=Y0ZqKpToTic

    1. start by building 2d array of size len(denominations)*total
    eg: denominations = [1, 5, 6, 8], total = 11

          index   0   1   2   3   4   5   6   7   8   9   10  11    # len = 12
        val rep   0   1   2   3   4   5   6   7   8   9   10  11
                  -----------------------------------------------
        1  1    | 0   1   x   3   4   5   6   7   8   9   10  11    # first row, do by itself
        2  5    | 0   y   2   3   4   z   l   .   .   .    .   3    # every other row builds on either the min from above
        3  6    | 0   1   2<  3   4   1   1   2   3<  4    2   2    # or back a number of places + 1
        4  8    | 0   1   2   3   4   1   1   2   1   2    2   2    # as to make 8 you need with coins of 6 and 1 you need one
                                                                    # 6 and two 1s, go back 6 places to get to 2<
        that gives us the number of coins to make 2 from coins (1, 5, 6) then + 1 representing adding a coin of value 6 resutling in 3<

   x is asking what is the minimum number of ways we can make a value of 1 with an unlimited supply of coins of value 1 = 1
   carry on like this for the first row

   y is asking what is the minimum number of ways we can make the value of 1 with an unlimited supply of coins of value 1, 5
    we can't do better so the value comes from the row above = 1

   z is asking what is the minimum number of ways we can make the value of 5 with an unlimited supply of coins of value 1, 5 = 1
    this comes from minimum of value above vs going 5 steps back to the value 0 + 1

   l is from going 5 steps backwards and adding 1
   this is because going 5 steps back we are saying we need one 5 coin and one 1 coin

   formula: if j >= coin[i]                                     # don't use this formula for the first row
            then table[i][j] = min (
                                    table[i-1][j],              # look at solution 1 row above and use that
                                    1 + table[i][j-coin[i]]     # take the solution coin[i] spaces to the left and add 1
                                    )
            else:
               table[i][j] = table[i-1][j]    # take row above value as we won't be able to use this new coin as value we are trying to make is (j) < the new coin


   How to pick out a formula like this?
    1. practice questions --> builds intuition on similar problems
    2. if we need to store lots of past calculations --> hints at dp
    3. extend a basic solution to something else some how
"""

def minimum_number_of_coins(coin_denominations, total):
    """
    :param coin_denominations: array of coins of different values
    :param total: total we need to make
    :return:
    """
    full_array_filled = False

    table = [[0 for _ in range(total + 1)] for _ in range(len(coin_denominations))]     # initialize the first column as 0 for each row, needed as need to loop to total + 1 (so total is looked at)

    for k in range(1, total+1):
        even_div = k % coin_denominations[0]
        if even_div == 0:
            table[0][k] = k // coin_denominations[0]
        else:
            table[0][k] = 0

    for i in range(1, len(coin_denominations)):     # i indexes the coin_denominations array and the row in the table
        for j in range(1, total + 1):               # we skip the 0th value of the ith row
            if j >= coin_denominations[i]:          # j indexes the sum we are trying to make <= total
                table[i][j] = min_bounded(table, coin_denominations, i, j)
                                              # does the above (prev) way take less coins?
                                #table[i][j - coin_denominations[i]] + 1    # value in current_col - value of coin + 1 (adding another coin of the same value)
                                 #   )                                      # want minimum number of coins


            else:
                table[i][j] = table[i-1][j]   # value above as we can't make it with the newest coin i.e. can't make value 3 with a coin of value 5
    [print(x) for x in table]
    coins_needed = find_coins(table, coin_denominations)    # find actual coins needed
    return table, coins_needed                      # final number of coins needed

def find_coins(table, coin_denominations):
    number_coins_needed = table[-1][-1]
    coins = []
    row, col = -1, -1
    to_find = number_coins_needed
    going_up = False
    while len(coins) != number_coins_needed:

        if row != -len(table):
            if table[row - 1][col] == to_find:                                  # check if it came from above
                # it came from the top, need to check where this one came from
                going_up = True
                #coins.append(coin_denominations[row - 1])
                #to_find -= 1
                row -= 1

        if col - coin_denominations[row] >= -len(table[0]):
            if table[row][col - coin_denominations[row]] == to_find - 1:      # check if it came from this row
                coins.append(coin_denominations[row])
                to_find -= 1
                if col - coin_denominations[row] == 0:                      # reached first column, means we are done
                    coins.append(coin_denominations[row])
                    break
                col = col - coin_denominations[row]
        else:
            row -= 1
            if row == 0:
                if col - coin_denominations[row] == 0:                      # reached first column, means we are done
                    coins.append(coin_denominations[row])
                    break

       # else:
        #    print("ERR")
    return coins

def min_bounded(table, coin_denminations, i, j):
    """
    we have the case where if anything = 0 it means we can't make that value of j
    additionally when checking in the same row to extend the solution, should check if the value is 0
    if so we can't just +1 to it

    if both value are 0, return 0
    else if both are > 0 return min
    else return the non zero one
    remembering to +1 if it is on the same row
    :return:
    """
    # table[i-1][j],table[i][j - coin_denominations[i]]+1

    # value from above row
    above = table[i - 1][j]
    # value from same row (already used coin_dem[i]
    same_row = table[i][j - coin_denminations[i]]   # don't +1 to this until later as if you do it at the start will lead to a false soln
    new = False
    if j % coin_denminations[i] == 0:
        new = j // coin_denminations[i]

    if above == 0 and same_row == 0:    # both can't make a solution
        if new:
            return new
        return 0                        # no solution
    elif above > 0 and same_row == 0:   # can make a solution using above value
        if new:
            return min(new, above)
        return above
    elif above == 0 and same_row > 0:   # can make a solution using value on same_row, remember to + 1
        if new:
            return min(new, same_row+1)
        return same_row + 1
    elif above > 0 and same_row > 0:    # pick min
        m = min(above, same_row + 1)    # remember to + 1 to same_row
        if new:
            return min(new, m)
        return m
    else:
        raise Exception

min_coins = minimum_number_of_coins([2,4,6],5)
table, coins = min_coins

#for row in table:
#    print(row)

print("Minimum number of coins: " + str(table[-1][-1]))
print("Coins used: " + str(coins))
# refactor this