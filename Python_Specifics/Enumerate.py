"""
@author: David Lei
@since: 22/08/2016
@modified: 

enumerate gives use the index as well as value in a tuple
(index, value) for each item in our list
"""

l = ['apple', 'google', 'microsoft', 'atlassian', 'dropbox', 'pokemon']

enum = list(enumerate(l))

print(enum)

for idx, value in enumerate(l):
    print(str(idx) + ", " + str(value))

