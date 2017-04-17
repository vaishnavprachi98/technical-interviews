# Python program to print all permutations with
# duplicates allowed
 
def toString(List):
    return ''.join(List)
 
# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l==r:
        print(toString(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack
 
# Driver program to test the above function
#string = "pokemon"
#n = len(string)
#a = list(string)
#permute(a, 0, n-1)
 
# This code is contributed by Bhavya Jain

def permutations(array, start, end):
    if start == end:                    # base case
        print(array)
    else:
        for i in range(start, end+1):
            array[start], array[i] = array[i], array[start]
            permutations(array, start + 1, end)
            array[start], array[i] = array[i], array[start]
s = list('lunch')
k = len(s)
permutations(s, 0, k-1)


print("Common elements")
print("YO GUHURT")