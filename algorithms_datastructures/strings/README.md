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
1. use a single character.
2. fix it in a configuration to generate substrings from that position
3. back track placing it back and getting another character.


## All sub-strings of length n to 1

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

## Longest Common Sub-sequence

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

## Palindromic DP