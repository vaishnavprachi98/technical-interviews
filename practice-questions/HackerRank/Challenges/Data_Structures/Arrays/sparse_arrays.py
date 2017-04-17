"""
@author: David Lei
@since: 14/04/2017
@modified: 

"""
number_elements, operations = [int(x) for x in input().split(' ')]

values = [0] * number_elements

# Solve with an array of differences instead of an array of values.

for _ in range(operations):
    index_start, index_end, value = [int(x) for x in input().split(' ')]
    values[index_start - 1] += value
    if index_end < number_elements:
        values[index_end] -= value

max_value = 0
current_value = 0
for n in values:
    current_value += n
    if current_value > max_value:
        max_value = current_value
print(max_value)

