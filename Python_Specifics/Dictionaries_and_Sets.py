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


"""
.sort
uses tim sort
http://stackoverflow.com/questions/10948920/what-algorithm-does-pythons-sorted-use

Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort, designed to perform well on many kinds of real-world data
timsort:
- worst case: O(n log n)
- best case: O(n)
- avg case: O(n log n)
worst case space: O(n)
- stable
"""
print("\nSorting via .sort()")

def random_array_permutation(a_list):
    import random
    for i in range(len(a_list)):
        radom_index = random.randint(i, len(a_list)-1)
        a_list[i], a_list[radom_index] = a_list[radom_index], a_list[i]

sort_me = [('a', 'Apple'), ('a', 'ABatman'), ('aba', 'Candy'), ('aa', 'Egg Yolk'), ('a', 'Frogs'), ('b', 'Gnome'), ('b', 'Appl'), ('b', 'Apple')]
print(sort_me)
random_array_permutation(sort_me)
print("after random permutation:                  " + str(sort_me))
sort_me.sort()
print(".sort(), default first item in the tup     : " + str(sort_me))       # sorts lexicographically via first element in tuple
sort_me.sort(key= lambda tup: tup[1])   # sort lexicographically via 2nd element in tuple (specified with lambada)
print(".sort(key=lambda t:t[1]) or 2nd item in tup: " + str(sort_me))
print("\nSetting the sorting prioirty in the lambda function, key = lambda a_tuple: (tuple_element_to_sort_by_first, tuple_element_to_sort_by_second)")
sort_me.sort(key = lambda tup: (tup[1], tup[0]))
print("\n.sort(key=lambda t:(t[1],t[0])             : " + str(sort_me))
"""
SETS
"""
print()
# note: to get a unique array of integers, can also use a set
# should check underlying implementation of set and dict

arr = [1,2,2,1,2,3,4,5,6,5,4,1,]
unique = set(arr)
print(unique)
for n in unique:
    print(n)
unique_to_list = list(set(arr))
print(unique_to_list)

# check O(complexity) of stack operations

# https://wiki.python.org/moin/TimeComplexity
# check something in a_set is O(1)

# https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
l = ['a','bee', 'cee', 'dee', 'eee', 'f', 'g']
s = set(l)
if 'b' in s:
    print('b')
if 'bee' in s:
    print('bee')