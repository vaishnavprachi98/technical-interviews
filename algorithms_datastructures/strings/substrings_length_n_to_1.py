"""
@author: David Lei
@since: 19/10/2017

"""
def substrings_of_length_n_to_1(string):
    count = 0
    print("length of input string: %s" % len(string))
    strings = []
    # Loop from 1 to len(string) - 1 inclusive, this is the length of the substring to produce.
    for i in range(1, len(string) + 1):
        # Loop for i to n to create substrings of length i, +1 to make it the upper bound extend to the length of the array capturing the last character.
        for j in range(0 , len(string) - i + 1):
            # Eg: string = 'apple'
            # In the first iteration it will find substrings of length 1 as it will loop from 0 to len(string) - 2 + 1
            # the last assignment to substring will be string[len(string) - 1: len(string)] which would be the last element.

            # In the last iteration it will find the substring of length n, it will loop from 0 to len(string) - n + 1 so just once.
            # the last assignment to substring will be string[0: len(string)]
            substring = string[j: j + i]
            strings.append(substring)
            count += 1
    print("inner loop executed: %s times" % count)
    return strings

if __name__ == "__main__":
    substrings = substrings_of_length_n_to_1("trees")
    print(substrings)
