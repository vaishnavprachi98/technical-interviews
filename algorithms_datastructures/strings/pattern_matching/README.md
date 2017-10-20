# Special String Things!

## KMP (Kunth Morris Pratt) Substring Search

Given a `text:"abcbcglx"` does the a `pattern: "bcgl"` exist in it.

Naive approach:
1. start i at 0th index of text
2. check for the length of the patter
3. if no match increment i
4. repeat

This is O(t * p) where t is the length of the text and p is the length of the pattern.

KMP can do it in O(t + p).

Key idea:
- uses suffix and prefix information to reduce comparisons

KMP Example:
```
text =    abcxdbcdabxabcdabcdabcy
pattern = abcdabcy

First non match at index 3 with 'x' from the text and 'd' from the pattern.
```
