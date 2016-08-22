"""
@author: David Lei
@since: 21/08/2016
@modified:

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
            - doesnt't work for negative nobe's
            - assumes each element is a small integer
            - O(max v - min v) which is O(n) if difference between min and max not too large

Invariants: when we get to merging, after the merge everything in that list will be sorted?

Compared to quick: work is done putting the array back together

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
    -
- best O(n log n)
- worst O(n log n)
- avg O(n log n)

Space complexity
- O(N), when we merge we copy so need another N space so O(N), also create new lists when we split?

Stability: yes as in merge we use > or < and not =

Note: no matter what the input is, the count always stays the same for arrays of the same length
- arr and bar are the same len, but different numbers. Both get a count of 13
- this reflects merge sort's best=worst=avg complexity
"""