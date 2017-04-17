"""
@author: David Lei
@since: 26/08/2016
@modified: 

"""
def bin_search_root_start(find, min, max):
     if min > find or max < find:
        return -1
     else:
         return binary_search_root2(find, min, max)
def binary_search_root2(find, min, max):
    # find square root of 2 using binary search

    if max <= min:
        return -1
    else:
        mid = (max + min)/2

        if round(mid*mid, 10) == find:
            return mid
        elif mid*mid > find:
            return binary_search_root2(find, min, mid)
        elif mid*mid < find:
            return binary_search_root2(find, mid, max)

print(binary_search_root2(5, 0, 10))