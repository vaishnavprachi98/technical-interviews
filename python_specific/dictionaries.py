"""
@author: David Lei
@since: 28/08/2016
@modified:


https://www.quora.com/How-is-set-implemented-internally-in-python

It is a hash table, implemented very similarly the Python dict with some optimizations
that take advantage of the fact that the values are always null (in a set, we only care about the keys).
Set operations do require iteration over at least one of the operand tables (both in the case of union).
Iteration isn't any cheaper than any other collection ( O(n) ), but membership testing is O(1) on average.

"""

"""
DICTS
"""

d = {}
d['a'] = 'Apple'
d['b'] = 'Batman'
d['c'] = 'Candy'
d['e'] = 'Egg Yolk'
d['f'] = 'Frogs'
d['g'] = 'Gnome'

for key in d:
    print(str("key: " + str(key) + ", value: " + str(d[key])))

print(d.keys())
print(d.values())
print(d.get('a'))
print(d.items())

print("Getting items form dict")
for an_item in d.items():
    print(an_item)
to_list = list(d.items())       # get items in a form nicely
print("Items from dict to list of tuples")
print(to_list)

for item in to_list:
    print("item: " + str(item) + ", key: " + str(item[0]) + ", value: " + str(item[1]))
print("\nRemoving elements form dictionary")
first_element = 'a', 'Apple'
d.pop('b')    # dictionary.pop(key, default)
#d.pop(first_element) won't work as only meant to pass key to pop
# remove and return the value of key, if not in, return default, else keyerror
print(d.items())


