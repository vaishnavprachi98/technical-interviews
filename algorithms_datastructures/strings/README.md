# Strings


Common questions:
- longest common prefix
- longest common sub sequence
- permutations
- palindrome questions (usually involes dp)

Less common questions:
- suffix related
- pattern matching

String questions typically involve some dp to optimize their brute for approaches.

## String permutations

Given a string get all permutations.

Key idea:
1. remove the first letter.
2. final all permutations of remaining letters (recursive step).
3. reinsert letter removed at every possible location

This can be done recursively.

```python

def permuate(string, permutation_holder, call_num):
    """Order is important in permutations.
    For a string of length n there are n! permutations.

    Args:
        call_num: used to help understand the complexity of the algorithm for each call print out the times the nested loop executes.
        string: the string to find permutations for.
        permutation_holder: list to append to holding permutations of string.
    """
    if len(string) <= 1:  # Base case, only 1 way to permute a string of length 1.
        permutation_holder.append(string)
        return
    first_char = string[0]
    sub_permutations = []
    permuate(string[1:], sub_permutations, call_num + 1)  # Recursive step to find all permutations of a substring of string (removing the first character).
    count = 0
    for sub_permutation in sub_permutations:
        # Put first_char in sub_permutation all ways possible.
        for i in range(len(sub_permutation) + 1):  # Careful for off by 1.
            permutation = sub_permutation[0:i] + first_char + sub_permutation[i:]
            permutation_holder.append(permutation)
            count += 1
    print("call_num: %s did nested loop %s times" % (call_num, count))
```

`permuate()` will be called once on a string of length n after fixing the first character.
It will be called again on a string of length n-1 until a string of length 2 then once more on a string of length 1 which will return the base case.

So `O(n)` calls.

There will be `n!` permutations for a string of length `n`.

Once returning from the base case `sub_permutations` will be a list of 1 string. it will go through the nested loop and add two strings to `permutation_holder`.
`permutation_holder` ends up being `sub_permutations` for the parent of this recursive call and will iterate through the two strings and then add another six strings to `permutation_hoder` as for each of the two strings of size two you can place a single character in it 3 ways.
This keeps going until `sub_permutations` has n-2 strings of length n-1, we then go through the nested loop and output `n!` strings.

Note that at the base case the nested loop never executes, at the recursive call right before the base case it only executes twice after that 3 times and so on.
it is not `n` calls each doing `n!` work. Each call will do at most `n!` work, adding `call_num` as an argument and printing out the count of the nested loop helps us understand the complexity more.

When permuting the string `apples`:
```
call_num: 5 did nested loop 2 times
call_num: 4 did nested loop 6 times
call_num: 3 did nested loop 24 times
call_num: 2 did nested loop 120 times
call_num: 1 did nested loop 720 times
```
This means the first call to the program executed the nested loop 720 times, but the second call only did it 120 times.
Note that 720 is 6! and 120 is 5! and so on.

So there were in total 6 calls to `permuate()` (base cases didn't bring) and each call does `(n - call_num)!` work.

Based on the numbers here we can see it is bounded by `n!` so the algorithm is `O(n!)`

## All substrings of length n to 1

Given a string print all contiguous sub-strings of length n, n-1 and so on until 1.

Key idea:
1. loop i from 1 to n - 1 inclusive for the length of the substring to produce.
2. loop j decrementing from i to n
3. print substring of length inner loop j starting at position i.

```python
def substrings_of_length_n_to_1(string):
    count = 0
    print("length of input string: %s" % len(string))
    strings = []
    # Loop from 1 to len(string) inclusive, this is the length of the substring to produce.
    for i in range(1, len(string) + 1):
        # Loop for i to n to create substrings of length i, +1 to make it the upper bound extend to the length of the array capturing the last character.
        for j in range(0 , len(string) - i + 1):
            # Eg: string = 'apple'
            # In the first iteration it will find substrings of length 1 as it will loop from 0 to len(string) - 2 + 1
            # the last assignment to substring will be string[len(string) - 1: len(string)] which would be the last element.
            # In the last iteration it will find the substring of length n, it will loop from 0 to len(string) - n + 1 so just once.
            # the last assignment to substring will be string[0: len(string)]
            substring = string[j: j + i]
            strings.append(substring)
            count += 1
    print("inner loop executed: %s times" % count)
    return strings
```

This works but you need to be careful with the bounds and off by 1 errors, it is hard to think of (and get right) under pressure.

Complexity is O(n) for the outer loop. In the first iteration of the outer loop the inner loop will be executed n times, in the second iteration of the outer loop it will execute n - 1 times and so on until it only executes once.
A loose upper bound is O(n^2), a tighter analysis is O(n + n + n - 1 + n - 2 + ... + 2 + 1). The first factor of n comes from the outer loop, the rest is the number of times the inner loop executes.

This is equivalent to [n(n + 1)/2](https://math.stackexchange.com/questions/2260/proof-for-formula-for-sum-of-sequence-123-ldotsn)

As if we let `S = n + n - 1 + n - 2 + ... + 2 + 1` if we write it backwards i.e. `S' = 1 + 2 + ... + n - 2 + n - 1 + n` and then add them we get
`S' + S = (n + 1) + (n - 1 + 2) + (n - 2 + 3) ... + (1 + n)` which simplifies to `2S = n + 1 + n + 1 ....` where the term `n + 1` occurs n times so
we can write it as `2S = n * (n + 1)` as we know the `1s` will sum to n and the n `ns` will sum to n * n. So the sum is `(n * (n + 1)) / 2`

So the complexity is O(n + (n^2 + n)/2) It is upper bounded by O(n^2) since we can discard 2 as it is a constant. All that math for nothing :(.

For a string of length 15 the inner loop executes 120 times, for a string of length 6 the inner loop executes 21 times which is exactly (15 * 15 + 15)/2 and (6 * 6 + 6)/2.

So the overall complexity is O(n^2).

## Longest Common Subsequence

A sub sequence is in the same order but it doesnt't need to be continuous.

Definition: A sub-sequence can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

The longest comm sub-sequence of 'abcdefg' and 'acjekfg' is 'acefg'.

A worked example:

For 2 strings build a table.

- `string_a = angpp`
- `string_b = apple`

Here the elements with an x are the same, they can either be used to extend the lcp or start a new lcp.

Note: $ is just the null string "".

```
This table just shows the same characters in the two strings marked by x.
   $ a p p l e
$  0 0 0 0 0 0
a  0 x 0 0 0 0
n  0 0 0 0 0 0
g  0 0 0 0 0 0
p  0 0 x x 0 0
p  0 0 x x 0 0
```

If it is a 0 then the character at the row has no lcp with the string on across the cols.
However the string across the rows the character belongs to might so we pick the min from above and to the left.

What a particular cell in our matrix is M[i][j] is the lcp for the `string_a[0:i]` and `string_b[0:j]`.
So when we increment `j` by 1 we are extending the part of `string_b` we are are looking at by 1 so we can take values to our left as it belongs to the same `string_b`.
When we increment `i` by 1 we are extending the part of `string_a` we are looking at by 1 and so can take values above as it belongs to the same `string_a`.

So the recurrence becomes max(previous_from_above, previous_from_left) if the chars being compared are not the same.

If they are the same then the top left diagonal box + 1 as we can add to the longest common subsequence.
This is saying these characters can add to the lcp, what is the best we can do without them? well to find that just go up one
row reducing string a by 1 and go left one column reducing string b by 1, so we are looking at without the new character, what is the best lcp we can make.

```
This table shows the final dp table.
   $ a p p l e
$  0 0 0 0 0 0
a  0 1 1 1 1 1
n  0 1 1 1 1 1
g  0 1 1 1 1 1
p  0 1 2 2 2 2
p  0 1 2 3 3 3
```
- `string_a` goes across rows meaning each row represents 1 char in `string_a`.
- `string_b` goes across columns meaning each col represents 1 char in `string_b`.

```python
def longest_common_subsequence(string_a, string_b, verbose=False):
    table = [[0 for _ in range(len(string_b) + 1)] for _ in range(len(string_a) + 1)]
    # We start from 1 and loop until length + 1 so we can look back at the 0th rows and cols
    # when checking the first chars of each string so we don't need to deal with special cases.
    for i in range(1, len(string_a) + 1):
        for j in range(1, len(string_b) + 1):
            if string_a[i - 1] == string_b[j - 1]:  # Can add char string_b[j - 1] to the lcp.
                best_without_this_char = table[i - 1][j - 1]
                table[i][j] = best_without_this_char + 1  # Add 1 as we take this char.
            else:
                # Can't take this char, just get max from above and below representing the best we could do previously as we can't add anything.
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    # Return the lcp, length of lcp is at table[-1][-1].
    r = len(string_a)  # string_a goes across rows, each row represents a char in string_a.
    c = len(string_b)  # string_b goes across columns, each col represents a char in string_b.
    string_array = []
    while True:  # Note: more than 1 solution can be found here.
        if table[r][c] == 0:
            break
        if table[r][c] == table[r - 1][c]:  # Check if the value came from above.
            r -= 1
        elif table[r][c] == table[r][c - 1]:  # Check if the value came from the left.
            c -= 1
        else:  # The current character is in the lcp, move up diagonally after.
            string_array.append(string_b[c - 1])  # -1 as the table has an extra row and col.
            r -= 1
            c -= 1
    return "".join(string_array[::-1])
```

The space and time complexity is O(a * b) where a is the length of string_a and b is the length of string_b.

## Longest common substring

Similar to above however a substring has to be continous.


## Palindromic DP