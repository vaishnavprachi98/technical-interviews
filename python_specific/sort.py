"""
@author: David Lei
@since: 19/10/2017

"""
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

# check O(complexity) of stack operations

# https://wiki.python.org/moin/TimeComplexity
# check something in a_set is O(1)
