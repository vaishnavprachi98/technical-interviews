"""
@author: David Lei
@since: 7/11/2017

https://www.hackerrank.com/challenges/equal-stacks/problem

Make all stacks equal by removing stuff from the top, empty stacks are still stacks.

Passes :)
"""

n1, n2, n3 = [int(x) for x in input().split()]
stack1 = [int(x) for x in input().split()]
stack1.reverse()
stack2 = [int(x) for x in input().split()]
stack2.reverse()
stack3 = [int(x) for x in input().split()]
stack3.reverse()

height1 = sum(stack1)
height2 = sum(stack2)
height3 = sum(stack3)

while not (height1 == height2 == height3):
    if height1 > height2:
        height1 -= stack1.pop()
    if height1 > height3:
        height1 -= stack1.pop()
    if height2 > height1:
        height2 -= stack2.pop()
    if height2 > height3:
        height2 -= stack2.pop()
    if height3 > height1:
        height3 -= stack3.pop()
    if height3 > height2:
        height3 -= stack3.pop()
print(height1)

# More efficient soln: https://www.hackerrank.com/challenges/equal-stacks/forum
# Make cumulative sum of values in stack order, loop through smallest array to find the first common value in all others
# that is the height of all stacks balanced.