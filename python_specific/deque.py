"""
@author: David Lei
@since: 19/10/2017

"""
from collections import deque

length_of_queue = 5
circular_queue = deque(maxlen=length_of_queue)

for i in range(10):
    circular_queue.append(i)
print(circular_queue)  # deque([5, 6, 7, 8, 9], maxlen=5)

drinks = ["water", "coffee", "v", "milk", "potato"]
d = deque(drinks)
print(d)      # deque(['water', 'coffee', 'v', 'milk', 'potato'])
d.rotate(2)   # rotate array elements 2 to the right.
print(d)      # deque(['milk', 'potato', 'water', 'coffee', 'v'])
d.rotate(-4)  # rotate array elements 4 to the left.
print(d)      # deque(['v', 'milk', 'potato', 'water', 'coffee'])

# reverse deque, need to make a new deque/loop over it as it returns an iterator
print(deque(reversed(d)))  # deque(['coffee', 'water', 'potato', 'milk', 'v'])

# iteration.
for i in reversed(d):
    print(i)

d.clear()    # Empty everything.
print(d)     # deque([])
