"""
@author: David Lei
@since: 20/10/2017

"""

stuff_was_done = [0, 0, 1, 1, 1, 0]
did_stuff = [1, 1, 1]
non_ones = [-4, 5]
print(any(stuff_was_done))  # True
print(all(stuff_was_done))  # False
print(all(did_stuff))  # True
print(all(non_ones))   # True
print("--")
print(any(stuff_was_done) == 1)  # True
print(all(stuff_was_done) == 1)  # False
print(all(did_stuff) == 1)  # True
print(all(non_ones) == 1)   # True

# >>> from fractions import gcd
# >>> gcd(20,8)
import math

print(math.gcd(60, 18))