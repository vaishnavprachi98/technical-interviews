# Dynamic Programming.

DP in a nutshell is using a memoization (a table/cache) to avoid recomputing repeated values.
 
It can be used in problems where:
- the optimal solution to the problem can be constructed from the optimal solution of sub problems.

This pretty much means the problem can be broken down in a divide and conquer like method where if you can solve the basic naive case you can propagate values up to solve more complex cases.
- the problem has overlapping sub problems.

This means there are repeated states in the problem that we can use DP to avoid re-computing.
- We only care about what we can do from the current sate, not how we got there.

This means that we don't care about the history at all. We do not care about we got to the current state, only how well we can do from the current state. This is helpful for identifying what states are important that we should include into our recursion.
So the question becomes how well can we do from our current state.

> Dynamic programming is all about ordering your computations in a way that you avoid recalculating duplicate work. You have a main problem (the root of your tree of sub problems), and sub problems (subtrees). The sub problems typically repeat and overlap.

## Approaches.

DP can be done top-down or bottom-up.

### Top Down DP.
- recursive with a memoization table
- easier to think about, more intuitive especially for programming competitions. You look at your state space and apply a brute force approach with a memoization table. This means it makes the problem easier to think about as you just consider your states.
- faster to code.

Starts at the top of your state tree. Recursive calls reduce problem size and cache computations. When the base case is reached propagate up, solutions to sub problems encountered on the path to the base case will not need to be re computed.

> Starts at the top of the tree and evaluates sub problems from leaves back up to the root.

### Bottom Up DP.
- iterative
- need to find recurance/relationship between states you are building in your DP table. This might not be intuitive.
- typically faster than recursion as you are not calling yourself many times.
- good for optimizing stuff.

Generally uses tabulation. 
A table finding algorithm similar to memoization but you need to chose order of computations ahead of time. 
> Need to consider entire state tree and evaluate sub problems in a particular order towards the root. 
Coming up with the ordering can be non intuitive like the coin chaining problem, where as in the down approach you can just - 1 the number of coins and do a brute force.

Quotes from: https://stackoverflow.com/questions/6164629/dynamic-programming-and-memoization-bottom-up-vs-top-down-approaches