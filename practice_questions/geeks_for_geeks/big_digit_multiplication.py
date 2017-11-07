"""
@author: David Lei
@since: 7/11/2017

http://www.geeksforgeeks.org/multiply-large-numbers-represented-as-strings/

Given two digits as strings, say you can't multiply them directly.
How do you calculate the product?

For each char in the 2nd digit, multiply it with the 1st and sum all results.

Note: need to loop backwards, not a very python related question.
"""

a = "1235421415454545454545454544"
b = "1714546546546545454544548544544545"

def mult(a, b):
    unit = "1"
    sums = []
    for i in range(len(b) -1, -1, -1):
        char = b[i]
        result = int(a) * int(char) * int(unit)
        unit += "0"
        sums.append(result)
    print(sums)
    return sum(sums)

print(mult(a, b))
print(int(a) * int(b))