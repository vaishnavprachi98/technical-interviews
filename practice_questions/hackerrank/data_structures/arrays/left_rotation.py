"""
@author: David Lei
@since: 4/11/2017


A left rotation shifts and element to the left, so if a value x at index i in array [y, x, z] is shifted to the left once it will result in
[x, z, y] meaning to get the new value at index i we can just look back i + number of times we do a left rotation % len to make sure we stay in bounds.

This works for index 2 as the new value after 2 left rotations is at index (2 + 2) % 3 = 1 which is x.
[y, x, z] -> [x, z, y] -> [z, y, x]

Passed :)
"""
n, d = [int(x) for x in input().split()]
array = [int(x) for x in input().split()]

def leftRotation(a, d):
    # d left rotations on array a.
    # Can either do actual rotation or just find the right values.
    # Finding the value is O(1) while doing actual left rotations is O(n) for each rotation.
    for i in range(len(a)):
        print(a[(i + d) % len(a)], end=" ")
