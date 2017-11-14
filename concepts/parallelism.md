# Parallelism

This only looks at algorithm parallelism at a high level, also has ties into distribution and handling large inputs that can't fit into memory (might be able to parallelize parts of the program, if you can then can send them to different machines and reduce the input size).

Is concurrently running the same program on multiple devices which can then be combined together to get the result.

This can be at the level of parallelism on a single host across multiple cores or across multiple hosts in a distributed environment.

Strategies include:
- shared memory
- message passing

An example could be [Bazel](https://github.com/bazelbuild/bazel) which can be used to distribute independent unit tests in one file across multiple machines.

> Parallelism is the process of processing several set of instructions simultaneously. It reduces the total computational time. Parallelism can be implemented by using parallel computers, i.e. a computer with many processors. Parallel computers require parallel algorithm, programming languages, compilers and operating system that support multitasking.

To make use of parallelism at the algorithm level we need a parallel algorithm.

> *Parallel Algorithm* − The problem is divided into sub-problems and are executed in parallel to get individual outputs. Later on, these individual outputs are combined together to get the final desired output.

The key take away is when a problem can be divided into sub-problems, this hints at **divide and conquer** paradigm.

Divide and conquer tends to be recursive where each recursive call is computed independently then joined up to form the answer.

This can be parallelized having multiple machines looking at a particular part of the subproblem.

For example if you have an array too big to fit into memory and you want to sort that you can use merge sort and divide it into half until it can fit in memory and send that part to a specific host, rinse and repeat then join up to form your answer.

Similarly **dynamic programming** can usually be modelled iteratively (bottom up) and recursively (top down) due to the nature of having overlapping subproblems.

It has [potential to be parallelized](https://stackoverflow.com/questions/1111938/parallel-dynamic-programming).

> IIRC, what you typically do with dynamic programming is to recursively divide a problem into subproblems, and assemble optimal solutions from optimal subsolutions. What makes it effective is that all optimal subsolutions are built into a cache so they need not be recomputed. If the problem can be divided several ways, you can fork the solver for each subsolution. If each(sub) problem averages 1+epsilon (for epsilon interestingly more than zero) possible subsolutions, then you'll get a lot of parallelism this way. You'll probably need locks on the cache entries to protect the individual solutions from being constructed more than once.

> We recently published a paper showing how to parallelize any d.p. on a shared memory multicore computer by means of a shared lock-free hash table:

[Radix Sort](https://en.wikipedia.org/wiki/Radix_sort#Application_to_parallel_computing) also has a recursive version (a recursively subdividing MSD radix sort) which can be parallelized.


