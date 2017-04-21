# Divide and Conquer Algorithms take form of

1. Divide - data set into smaller components
2. Conquer - solve smallest components
3. Combine - solutions to smaller components to form solution

Divide and conquer (D&C) is an algorithm design paradigm based on 
*multi-branched recursion*. 

A divide and conquer algorithm works by 
recursively breaking down a problem into two or more sub-problems 
of the same or related type, until these become simple enough to be 
solved directly. 

The solutions to the sub-problems are then combined to give a solution 
to the original problem.

Examples:

- Merge Sort
- Quick Sort
- Binary Search (Pesudo divide and conquer technique, only 1 half is processed)
> http://stackoverflow.com/questions/8850447/why-is-binary-search-a-divide-and-conquer-algorithm
Data Structures and Algorithm Analysis in Java, 2nd edtition, Mark Allen Weiss
Says that a D&C algorithm should have two disjoint recursive calls. I.e like QuickSort. Binary Search does not have this, even if it can be implemented recursively.
- Strassen's Matrix Multiplication (matrix multiplication) 
- Closest pair (points)
- Fast Fourier Transform 

Further reading: http://www.geeksforgeeks.org/divide-and-conquer-set-1-find-closest-pair-of-points/