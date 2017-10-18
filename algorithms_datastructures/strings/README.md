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
2. place it everywhere to generate a new string.
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
    # Loop from 1 to len(string) - 1 inclusive, this is the length of the substring to produce.
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

## Longest Common Sub Sequence

## Palindromic DP