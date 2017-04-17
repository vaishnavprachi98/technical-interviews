"""
@author: David Lei
@since: 26/08/2016
@modified: 

"""

S = 'abcdefg'
s = list(S)

def reverse_string(input_s):
    s = list(input_s)
    for i in range(len(s)//2):
        s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
        print(s)
    print(s)
    return "".join(s)
print(reverse_string(S))
"""
Method 1:

def method1():
  out_str = ''
  for num in xrange(loop_count):
    out_str += `num`
  return out_str
Method 4:

def method4():
  str_list = []
  for num in xrange(loop_count):
    str_list.append(`num`)
  return ''.join(str_list)
Now I realise they are not strictly representative, and the 4th method appends to a list before iterating through and joining each item, but it's a fair indication.

String join is significantly faster then concatenation.

Why? Strings are immutable and can't be changed in place. To alter one, a new representation needs to be created (a concatenation of the two).

String not mutable, this will give a type error
S[0] = 'x'
print(S)
"""