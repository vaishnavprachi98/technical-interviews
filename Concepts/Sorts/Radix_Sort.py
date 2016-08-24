"""
@author: David Lei
@since: 21/08/2016
@modified: 

Non comparison sorting algorithm

How it works:
    Least significant digit radix sort:
        - shorter keys before longer
        - keys of same len sorted lexicographically
        eg: sorted result = 1, 2, 3, 9, 10, 11 (so normal order of integer representations)

    Most significant digit radix sort:
        - uses lexicographical order suitable for strings
        eg: sorted result = "b, ba, c, d, e, f, g, ga, gaa, i"
        if used on integers with variable length, 1 - 10 will be
            sorted result = 1, 10, 2, 3, 4,.., 8, 9
            will need to left justify values and pad them to make same length as longest

Time Complexity: O(d(n + k)) where O(n + k) is time for inner stable sort --> O(n)

    - given n d digit numbers in which each digit can take up to k possible values (alphabet restriction)
        takes O(d(n+k)) if the stable sort takes O(n+k) time

            - k is the range from 0..k-1 that each digit can take (alphabet restriction)
                in counting sort k is the range, but as we look at 1 digit at a time, that 1 digit has to be in a
                specific range i.e. 0-9 for integers a-z for alphabet so k is that range
            - d is the number of digits in the number (100 will have d = 3)

            when d is a constant (i.e. sorting only 8 digit numbers) and k = O(n) or less (i.e. is the alphabet of
            integers 1-9) we can make radix sort run in linear time

            when digit d is in the range 0..k-1 and k is not too large, counting sort is a good choice
            each pass over n number of d digits takes O(n+k) time
            there will be d passes (to sort from least sig digit to most sig digit)
            so O(d(n+k)) or O(d(inner_stable_sort_time))

            so  O(n * d + n * k) for n keys of size d digits (number of characters i.e. 11 = 2 digits) with k
            the range of the alphabet for each digit, in application i.e. sorting 10 digit IDs
                - k will be a constant, 0-9
                - d will be a constant, 10
                so we can achieve O(n) time

            can also think about it as
            The running time is O (p(N + b))
            where p is the number of passes, N is the number of elements to sort, and b is the number of buckets.
            - passes depend on digits in that number (d)
            - 1 bucket for each element in the alphabet (or range) of each digit (k)

            note: http://www.geeksforgeeks.org/radix-sort/
             Radix Sort takes O(d*(n+b)) time where b is the base for representing numbers
             for example, for decimal system, b is 10
             - so if base = 10 and d is set as well we can make them out to be constants

Space Complexity: O(n + k)
    - count array of size k (10), k is the number of subdivisions or alphabet or range which for decimals is [0-9]
    - output and copy array of size n
    O(2n + k)

Stability: yes as iterating backwards when you put back into output array (like in counting sort)

Lemma 8.3
Given n d -digit numbers in which each digit can take on up to k possible values,
 RADIX-SORT correctly sorts these numbers in ‚.d.n C k// time if the stable sort it uses takes ‚.n C k/ time.
Proof The correctness of radix sort follows by induction on the column being sorted (see Exercise 8.3-3).
The analysis of the running time depends on the stable sort used as the intermediate sorting algorithm.
When each digit is in the range 0 to k 1 (so that it can take on k possible values), and k is not too large,
counting sort is the obvious choice. Each pass over n d -digit numbers then takes time ‚.n C k/. There are d passes, and so the total time for radix sort is ‚.d.n C k//.
When d is constant and k D O.n/, we can make radix sort run in linear time. More generally, we have some flexibility in how to break each key into digits.

Notes:

lexicographical order = dictionary order

consider the numbers: 15, 20, 33, 12, 21, 11, 31, 13
to sort these
    a) most sig value first:        15, 12, 11, 13, 20, 21, 33, 31
        then least sig:             20, 11, 21, 32, 12, 33, 13, 15
    b) least sig value first:       20, 11, 21, 31, 12, 13, 33, 15
        then most sig:              11, 12, 13, 15, 20, 21, 31, 33  # lexicographically sorted

so sort LBD then move towards MSD (Least sig dig first leads to stable correct sort)

This helps: https://www.cs.usfca.edu/~galles/visualization/RadixSort.html (implementation based off)
"""

def radix_sort_decimals(arr):
    """Radix sort implementation for integers
        d = len(str(max_value))
        k = 10 as decimals (base 10)"""

    max_value = max(arr)                                        # use to know number of digits
    digits = len(str(max_value))                                # found d

    arr_copy = [p for p in arr]                                 # copy arr so we can update this at each pass
    counting_sort_num = 0
    for i in range(1, digits+1):                                # loop for the number of digits in max_value, start at first digit (largest)
                                                                # using str(num)[-1] for last digit
        counting_sort_num += 1
        # run a counting sort to sort least sig digit to most sig digit (value of i)
        # need for each pass of counting sort

        counts = [0 for _ in range(10)]
        output = [0 for _ in range(len(arr_copy))]               # array of same size as input

        for j in range(len(arr_copy)):

            current_number = arr_copy[j]                         # find current digit we are looking at
            if len(str(current_number)) >= i:                    # get digit in number we care about
                digit_to_consider = int(str(current_number)[-i]) # this is an integer in range 0-9
            else:
                digit_to_consider = 0
            index = digit_to_consider                            # use this as index to count

            counts[index] += 1

        for l in range(1, len(counts)):                          # get cumulative sum of counts
            counts[l] += counts[l-1]

        for x in range(len(arr_copy)-1, -1, -1):                 # move items into output array stably (iterate backwards) based on counts
            current_number = arr_copy[x]
            if len(str(current_number)) >= i:                    # get digit we care about, use this to look up counts
                                                                 # array
                digit_to_consider = int(str(current_number)[-i])
            else:
                digit_to_consider = 0
            output_idx = counts[digit_to_consider] -1
            try:
                output[output_idx] = arr_copy[x]
                counts[digit_to_consider] -= 1
            except IndexError:
                pass
        arr_copy = output
        # completed once pass of O(n + k) counting sort, k is range or in this case size of alphabet (possible values)
        # which is [0-9] so 10
    return arr_copy

if __name__ == "__main__":
    arr = [11, 2, 90, 3, 413, 12, 2, 1, 1, 0, 1, 8, 19, 9866, 8787, 34, 413, 523, 138, 123]
    radix_result = radix_sort_decimals(arr)
    print("Radix sort result: " + str(radix_result))
    arr.sort()
    print("To check against:  " + str(arr))
    if arr == radix_result:
        print("True")
    else:
        print("False")