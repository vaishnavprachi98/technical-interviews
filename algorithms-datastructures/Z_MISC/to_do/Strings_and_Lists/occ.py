"""
@author: David Lei
@since: 29/08/2016
@modified: 

"""
# reverse string
# O complexities

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count
def oc(string, substring):
    count = 0
    start = 0
    while True:
        lowest_index_found = string.find(substring, string)
        start = lowest_index_found + 1                          # already found in this situation
        # will return - 1 if not found
        # so start will == 0
        if start > 0:
            count += 1
        else:
            return count


print(occurrences('banana', 'ana'))