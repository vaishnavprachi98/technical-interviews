"""
@author: David Lei
@since: 21/08/2016
@modified: 

"""

def joinWords(list_of_strings):
    sentence = ""
    for string in list_of_strings:
        sentence = sentence + string    # string concatenation
                                        # new copy of sentance
                                        # as strings are immutable
    return sentence

l = ["Hi ", "there ", "Bob!"]
print(joinWords(joinWords(l)))

"""
In this approach strings are copied over and over character by character
First iteration copies x characters
second iteration 2x
third iteration 3x
total time is O(x+2x+3x+.+nx) so complexity = O(xn^2)
note: 1 + 2 + 3 + .. + n =
"""

