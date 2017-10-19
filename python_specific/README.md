# Under the snake (python internals)

source: https://wiki.python.org/moin/TimeComplexity

## List

Important
- represented as an array
- big cost in growing beyond allocation size
- big cost in inserting near the begging as need to shift elements right

Gotchas
- slicing is O(k) and exclusive on the right bound
- `min()`, `max()` is O(n)

## Deque

Important
- list like with fast `append()` and `pop()` from both sides (`append()`, `appendleft()`, `pop()`, `popleft()`)
- can also extend on both sides

## Set

Important
- like dicts with similar implementation
- O(n) worst case look up

```python
list = [1, 2, 3, 4, 5, 6, 7, 7, 7, 8]
my_set = set(list)
your_set = set([1, 2, 100, 8, 7])
their_set = {7, 8, 9, 199}

print("my set: %s" % my_set)
print("your set: %s" % your_set)
print("their set: %s" % their_set)

# Unique values between sets.
difference = my_set - your_set  # {3, 4, 5, 6, 7, 8}
print("unique values (difference) in my set but not in your set: %s" % difference)

# Intersection between sets.
intersection = my_set & your_set
print("intersection between my set and your set: %s" % intersection)  # {1, 2}

# Union of two sets
union = my_set | your_set
print("union between my set and your set: %s" % union)  # {1, 2, 3, 4, 5, 6, 7, 8, 100}

# Values in set a or set b but not in both.
appears_once_in_both = my_set ^ your_set
print("appears in either my set or your set but not both: %s" % appears_once_in_both)  # {3, 100, 4, 5, 6}

# Comprehension.
big_list_of_things = ["apple", "pear", "banana", "table", "mouth", "mouse", "hair"]
things_that_are_not_fruit = {"table", "mouth", "mouse", "hair"}
fruit = {thing for thing in big_list_of_things if thing not in things_that_are_not_fruit}
print("fruit: %s" % fruit)

# Iteration over set.
for f in fruit:
    print(f)
```

## Dictionary

Important
- average case times listed for dict objects assume that the hash function for the objects is sufficiently robust to make collisions uncommon.
- get, set, delete all O(n) worst case.

