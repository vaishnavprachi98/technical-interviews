"""
@author: David Lei
@since: 19/10/2017

"""

def longest_common_subsequence(string_a, string_b, verbose=False):
    """Example:

    for 2 strings apple and anapp, build a table.

    Here the elements with an x are the same, they can either be used to extend the lcp or start a new lcp.

    Note: $ is just the null string "".

       $ a p p l e
    $  0 0 0 0 0 0
    a  0 x 0 0 0 0
    n  0 0 0 0 0 0
    g  0 0 0 0 0 0
    p  0 0 x x 0 0
    p  0 0 x x 0 0

    string a = angpp
    string b = apple

    If it is a 0 then the character at the row has no lcp with the string on across the cols.
    However the string across the rows the character belongs to might.
    What a particular cell in our matrix is M[i][j] is the lcp for the string a[0:i] and b[0:j] given our inputs are a and b.
    So when we extend j by one we can take values to our left as it belongs to the same string b.
    When we extend i by 1 we can take values above as it belongs to the same string.

    So the recurrence becomes max(previous_from_above, previous_from_left) if the chars being compared are not the same.

    If they are the same then the top left diagonal box + 1 as we can add to the longest common subsequence.
    This is saying these characters can add to the lcp, what is the best we can do without them? well to find that just go up one
    row reducing string a by 1 and go left one column reducing string b by 1.

       $ a p p l e
    $  0 0 0 0 0 0
    a  0 1 1 1 1 1
    n  0 1 1 1 1 1
    g  0 1 1 1 1 1
    p  0 1 2 2 2 2
    p  0 1 2 3 3 3

    string a goes across rows meaning each row represents 1 char in string a.
    string b goes across columns meaning each col represents 1 char in string b.
    """
    table = [[0 for _ in range(len(string_b) + 1)] for _ in range(len(string_a) + 1)]
    # We start from 1 and loop until length + 1 so we can look back at the 0th rows and cols
    # when checking the first chars of each string so we don't need to deal with special cases.
    for i in range(1, len(string_a) + 1):
        for j in range(1, len(string_b) + 1):
            if string_a[i - 1] == string_b[j - 1]:  # Can add to the lcp.
                if verbose:
                    print("Can add: %s to the lcp" % string_b[j - 1])
                best_without_this_char = table[i - 1][j - 1]
                table[i][j] = best_without_this_char + 1  # Add 1 as we take this char.
            else:
                # Can't take this char, just get max from above and below representing the best we could do previously as we can't add anything.
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    if verbose:  # Print out a nice table with the strings in it to see the dp table.
        print("lcp length: %s" % table[-1][-1])
        string_b_across_cols = ['[ $']
        string_b_across_cols.extend(["   " + c for c in string_b])
        string_b_across_cols.append("]")
        print("".join(string_b_across_cols))
        for i in range(len(table)):
            row_copy = table[i][::]
            row_copy.insert(0, string_a[i - 1] if i > 0 else "$")
            print(row_copy)
    # Return the lcp, length of lcp is at table[-1][-1].
    r = len(string_a)  # string_a goes across rows, each row represents a char in string_a.
    c = len(string_b)  # string_b goes across columns, each col represents a char in string_b.
    string_array = []
    while True:  # Note: more than 1 solution can be found here.
        if table[r][c] == 0:
            break
        if table[r][c] == table[r - 1][c]:  # Check if the value came from above.
            r -= 1
        elif table[r][c] == table[r][c - 1]:  # Check if the value came from the left.
            c -= 1
        else:  # The current character is in the lcp, move up diagonally after.
            if verbose:
                print("constructing lcp: (%s, %s) char: %s" % (r, c, string_b[c - 1]))
            string_array.append(string_b[c - 1])  # -1 as the table has an extra row and col.
            r -= 1
            c -= 1
    return "".join(string_array[::-1])

def hackerrank_submission(): # Copy this into main.
    # Note: Doesn't deal with integers > 9 so got wrong on some.
    len_a, len_b = [int(x) for x in input().split(' ')]
    string_a = "".join(input().split(' '))
    string_b = "".join(input().split(' '))
    lcp = longest_common_subsequence(string_a, string_b)
    for char in lcp:
        print("%s " % char, end="")

if __name__ == "__main__":
    string_a = "angpp"
    string_b = "apples"
    lcp = longest_common_subsequence(string_a, string_b, True)
    print("\n~~ Testing: string_a=%s, string_b=%s" % (string_a, string_b))
    print("lcp: \'%s\' is correct: %s" % (lcp, lcp == "app"))

    string_a = "agcat"
    string_b = "gac"
    lcp = longest_common_subsequence(string_a, string_b, False)
    print("\n~~ Testing: string_a=%s, string_b=%s" % (string_a, string_b))
    print("lcp: \'%s\' is correct: %s" % (lcp, lcp == "ac"))

    string_a = "who dat who dat, what u going to do when they come for you?"
    string_b = "whom's data? i will come for you..or will i?"
    lcp = longest_common_subsequence(string_a, string_b, False)
    print("\n~~ Testing: string_a=%s, string_b=%s" % (string_a, string_b))
    print("lcp: \'%s\' is correct: %s" % (lcp, lcp == "who data i w come for you?"))


    string_a = "abcdefg"
    string_b = "acjekfg"
    lcp = longest_common_subsequence(string_a, string_b, False)
    print("\n~~ Testing: string_a=%s, string_b=%s" % (string_a, string_b))
    print("lcp: \'%s\' is correct: %s" % (lcp, lcp == "acefg"))

