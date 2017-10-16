# Suffix Array
A suffix array is a sorted array of all suffixes of a given string.

Eg: 'banana' has the following suffixes:

| index | suffix |
|---|---|
| 0 | banana |
| 1 | anana |
| 2 | nana |
| 3| ana |
| 4| na |
| 5 | a |

This tells us that the 'nana' is the suffix from index 2.

This information is stored in a suffix array which is sorted lexicographically (alphabet ordering).

| index | stores | corresponding suffix |
|---|---|---|
| 0 | 5 | a |
| 1 | 3 | ana |
| 2 | 1 | anana |
| 3 | 0 | banana |
| 4 | 4 | na |
| 5 | 2 | nana |

`suffix_array = [5, 3, 1, 0, 4, 2]` this corresponds to `['a', 'ana', 'anana', 'banana', 'na', 'nan']`

We can now use binary search to find if a string/prefix is in the suffix array.

## Creation
Creating a suffix array: `n` elements, `O(n log n)` to sort but since we are sorting strings we multiply by a factor of `n` as in the worst case we compare `n` characters to `n-1` (e.g. when comparing 'banana' and 'anana') = `O(n^2 log n)`

## Pattern matching (searching)
Searching for a pattern using Suffix Array asks the question is my pattern `P` in the string `S`.
Using a suffix array we can check in `O(log n)` as it is sorted to see is there any suffix starting with/containing `P`. However since we are comparing strings we have to do `len(P)` work to check if a suffix contains `P` so `O(P * log n)`.

# TODO
- [x] naive suffix array
- [ ] number of occurrence a pattern occurs (I think this is upper and lower bound binary search)
- [ ] optimal suffix array with longest common prefix processing
- [ ] longest repeating substring
- [ ] suffix trie
- [ ] suffix automaton
- [ ] comparison of all these structures (for competition either should be fine)
- [ ] understand these
    - https://www.youtube.com/watch?v=x6j44AtzFmU&ab_channel=MiNiWolF
    - https://www.youtube.com/watch?v=HKPrVm5FWvg&ab_channel=AlgorithmsandDataStructures

