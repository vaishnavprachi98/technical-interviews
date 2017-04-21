"""
@author: David Lei
@since: 22/04/2017
@modified: 

https://www.hackerrank.com/challenges/sparse-arrays

This question can be done without sparse arrays :(
"""
import collections
num_strings = int(input())
string_map = collections.defaultdict(int)

for _ in range(num_strings):
    string = input()
    string_map[string] += 1

queries = int(input())
for _ in range(queries):
    q = input()
    print(string_map[q])
