"""
@author: David Lei
@since: 21/10/2017

http://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/

Given an square matrix, turn it by 90 degrees in anti-clockwise direction without using any extra space.

Input
 1  2  3
 4  5  6
 7  8  9

Output:
 3  6  9
 2  5  8
 1  4  7

Input:
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16

Output:
 4  8 12 16
 3  7 11 15
 2  6 10 14
 1  5  9 13
"""

def rotate_matrix(matrix):
    max_len = len(matrix)
