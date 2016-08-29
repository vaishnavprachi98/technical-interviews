"""
@author: David Lei
@since: 27/08/2016
@modified: 


Given a string, what is the longest palindrome in it
i.e. given 'bananas' the longest palindromic substring is 'anana'
Can be done in
- O(n^3) via brute force, take all substrings of length 1 to n, check if it is a palindrome
- O(n^2) via dynamic programming
- O(n) via Manacher's algorithm
"""

def longest_palindromic_substring_brute(s):
    l = len(s)
    best_pal = ""
    max_length = 0                      # keep track of len of max palindrome so far
    for i in range(1,len(s)+1):
        for j in range(len(s)+1-i):
            test_string = s[j:j+i]
            pal = True
            if len(test_string) != 1:
                for c in range(len(test_string)//2):
                    if test_string[c] == test_string[len(test_string)-1-c]:
                        pass
                    else:
                        pal = False
                        break
            if pal:
                if len(test_string) > max_length:
                    max_length = len(test_string)
                    best_pal = test_string

    return best_pal if best_pal != "" else -1


def longest_palindromic_substring_db(s):
    table = [[0]*(len(s)+1) for _ in range(len(s)+1)]
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] == s[j]:
                table[i+1][j+1] = True
            else:
                table[i+1][j+1] = False
    for row in table:
        print(row)
    pass


def longest_palindromic_substring_linear(s):
    pass

if __name__ == "__main__":
    #print(longest_palindromic_substring_brute("abbalomomomoz"))
    print(longest_palindromic_substring_db("bananas"))
print("YO GUHURT")