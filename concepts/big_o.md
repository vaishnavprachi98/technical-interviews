# Some Notes on Big O Complexities

## O(log n)

Material from: https://stackoverflow.com/questions/9152890/what-would-cause-an-algorithm-to-have-olog-n-complexity

When a problem size is repeatably divided by 2 it is usually a O(log n) algorithm.

Consider an input size of 128, divide this by 2 repeatably.
```
step 1: 128 / 2 = 64
step 2:  64 / 2 = 32
step 3:  32 / 2 = 16
step 4:  16 / 2 = 8
step 5:   8 / 2 = 4
step 6:   4 / 2 = 2
step 7:   2 / 2 = 1
```
This took 7 steps. Dividing a number `n` by `2` `i` times until 1 results in `1 = n/2^i`, when solving for `i` we get:
```
1: 1 = n/2^i
2: 2^i = n
2: log2 n = i
```
>In other words, if we pick an integer i such that i ≥ log2 n, then after dividing n in half i times we'll have a value that is at most 1. The smallest i for which this is guaranteed is roughly log2 n, so if we have an algorithm that divides by 2 until the number gets sufficiently small, then we can say that it terminates in O(log n) steps.

This typically follows the divide and conquer paradigm which divides the problem set up by cutting it each time and then conquering it by putting it together.
So algorithms that use divide and conquer typically have a O(log n) factor.

Note: Divide and conquer also should be parallelizable as at each step only what subproblem is considered.

TLDR: dividing by 2 or throwing away half the problem size results can only be done at most `i` times before we run out of data elements to discard, thus resulting in log base 2 n complexity O(log n).
