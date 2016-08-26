"""
@author: David Lei
@since: 26/08/2016
@modified: 

"""
import random
def permute_array(A):
    for i in range(len(A)):
        j = random.randint(i,len(A)-1)
        A[i], A[j] = A[j], A[i]
    return A