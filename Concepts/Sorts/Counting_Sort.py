"""
@author: David Lei
@since: 21/08/2016
@modified:

Not a comparison sort, so comparison O(n log n) lower bound doesn't apply

Visualization: https://www.cs.usfca.edu/~galles/visualization/CountingSort.html

How it works: Integer sorting algorithm - it counts the number of objects
                Applies when elements to be sorted come from a finite set i.e. integers 0 to k
                create an array of buckets to count how many times each element has appeared --> then place back in right order

            example: arr = [7, 1, 5, 2, 2]
            1. create array of buckets (size of max value +1) or of size k+1 where k is the max value in our set to sort
                    buckets = [[], [], [], [], [], [], [], []] # k + 1 buckets, k = 7
            2. count each element, look at the element in the input arr and put it in corresponding bucket
                    buckets = [[0], [1], [1,1], [0], [0], [1], [0], [1]]    # visual rep
                    buckets = [ 0,   1,    2,    0,   0,   1,   0,   1]     # actual rep
                    index:     0    1     2     3    4    5    6    7
                    means that we have zero 0's, two 2's, one 7 etc
            3. add up number of elements in the bucket array left to right (cumulative sum)
                    buckets = [0, 1, 3, 3, 3, 4, 4, 5]  # buckets[-1] == len(input_arr)
            4. put them back to output
                a) loop over input_arr
                b) find index of element in input arr in bucket (or count arr)
                c) put that element of input_arr into output arr in the index specified in bucket (after adding counts)
                    output = [?, ?, ?, ?, ?]           # same len as input
                    input = [7, 1, 5, 2, 2]
                    buckets = [0, 1, 3, 3, 3, 4, 4, 5] # after counting
                        idx    0  1  2  3  4  5  6  7
                    put 7 in index 5-1 (look at idx 7 of buckets) of output, decrement buckets[7] by 1
                    output = [?, ?, ?, ?, 7]
                              0  1  2  3  4
                    then do the same for 1 (idx 1 of input arr)

                    output = [1, ?, ?, ?, 7]
                    -->     [1, ?, ?, 5, 7]
                    -->     [1, ?, 2, 5, 7] # first 2 in input goes in idx 2 (then decrement value at idx 2 in bucket)
                    -->     [1, 2, 2, 5, 7] # second 2 in input goes in idx 1
                                            # so not stable if iterating over the unsorted array forwards
            ! iterating backwards over the sorted array will be stable
                above example iterating backwards
                    output = [?, ?, ?, ?, ?]
                    input = [7, 1, 5, 2!, 2*]
                    buckets = [0, 1, 3, 3, 3, 4, 4, 5]
                     idx       0  1  2  3  4  5  6  7

                    look at input[-1], it is 2, look at index 2 of buckets, it is 3, put 2 in index 3-1 of output
                    output = [?, ?, 2*, ?, ?]    now decrement buckets[2] by 1 so buckets = [0, 1, 2, 3, 3, 4, 4, 5]
                    -->      [?, 2!, 2*, ?, ?]   repeat, it has now it is stable
                    -->      [?, 2, 2, 5, ?]
                    -->      [1, 2, 2, 5, ?]
                    -->      [1, 2, 2, 5, 7]     done!

    Note:
            - doesnt't work for negative numbers
            - assumes each element is a small integer
            - O(max v - min v) which is O(n) if difference between min and max not too large

Time complexity
- dependent on number of buckets
    fast when data being sorted can be distributed between buckets evenly, if values sparse allocated then bigger buckets
    if values are dense, smaller buckets i.e.
        [2034, 33, 1001] --> bucket size around 1000
        [100,90,80,70,110] --> smaller bucket size ideal
Good when:
    - additional O(n+k) memory not an issue, n to copy array, k for the number of buckets(?)
    - elements expected to be fairly evenly distributed
    - as k is a constant for a set number of buckets, when small it gives O(n) performance
Bad when:
    - all elements are put into the same bucket
    - individual buckets are sorted, if everything put into 1 bucket, complexity dominated by inner
    sorting algo(?)

- first loop to count occurrences is always O(n)
- second loop to cumulative sum occurrences is always O(k+1) where k is the number such that all values lay in 0..k
- third loop to put elements in input in the right position of output is always O(n)
so overall O(2n + k + 1) = O(n+k) which is linear (best = worst = avg)

Space complexity
- with just input arr it is O(1)
- we make a solution array (or output) which is the same size as input O(n)
- we also have an array for the buckets or counts which is the range of smallest to biggest which is of size k+1
so overall O(n + k) space complexity

When the max value difference is significantly smaller than number of items, counting sort is really efficient

Stability: yes when you put elements from input to output backwards

Note: no matter what the input is, the count always stays the same for arrays of the same length
- arr and bar are the same len, but different numbers. Both get a count of 13
- this reflects merge sort's best = worst = avg complexity
"""

def counting_sort(arr):
    c1, c2, c3 = 0, 0, 0

    # set up
    max_number = max(arr)
    count = [0] * (max_number+1)            # is the array of "buckets" which starts at 0 and goes to max+1
    output = [0] * len(arr)

    # count occurrences of each number in arr and put it in 'bucket' in count
    for number in arr:                      # the item at index number of count += 1 to found occurrence of that number
        count[number] += 1

        c1 += 1

    # cumulative sum of occurrences
    for i in range(1, len(count)):          # cumulative sum
        count[i] += count[i-1]

        c2 += 1

    # put into output stably
    for j in range(len(arr)-1, -1, -1):       # work backwards to keep stable
        output_idx = count[arr[j]] - 1      # -1 as output len = arr len
        output[output_idx] = arr[j]         # put in right place in output
        count[arr[j]] -= 1                  # decrement value in count

        print(output)
        c3 += 1

    print("first loop: " + str(c1) + "\nsecond loop: " + str(c2) + "\nthird loop: " + str(c3))
    """
    for array [7,1,5,2,2] len = 5, range of values from 0 = 0 to 7
    the algorithm is
    O(len) to count (and find max?)
    O(range) for cumulative sum
    O(len) to copy back

    so O(3n + k) = O(n)

    if the range is big (like in big_arr), the complexity is dominated by k

    however in application, k usually small
    """
    return output

if __name__ == "__main__":
    #arr = [7,1,5,2,2]
    #big_arr = [100,101,101,105,104,103]#[1,1,1,1,2,3,3,4,5,6,7,8,9,10,11,100,150,160,170,200,300,650]
    test_arr = [1,2,3,4,5,6]
    counting_sort(test_arr[::-1])







