"""
@author: David Lei
@since: 4/11/2017

https://www.hackerrank.com/challenges/dynamic-array/problem

Create a list of N empty sequences (lists) and an integer lastAnswer = 0, supporting 2 types of queries:
- 1 x y: find sequence at index ((x xor lastAnswer) % N) and append y to that sequence
- 2 x y: find sequence at index ((x xor lastAnswer) % N), find the value of index y % size(seq) in seq and assign that to lastAnswer, print lastAnswer

Passed :)
"""

last_ans = 0
n, q = [int(d) for d in input().split()]
seq_list = [[] for _ in range(n)]
for _ in range(q):
    query_type, x, y = [int(d) for d in input().split()]
    if query_type == 1:
        seq_list[(x ^ last_ans) % n].append(y)
    else:
        l = seq_list[(x ^ last_ans) % n]
        last_ans = l[y % len(l)]
        print(last_ans)