"""
@author: David Lei
@since: 21/08/2016
@modified:

Visualization: https://www.cs.usfca.edu/~galles/visualization/BucketSort.html

a.k.a bin sort

How it works: puts elements of array into buckets, each bucket sorted individually (by another sorting algo or
                recursively applying bucket sort)
            1. Set up array of empty "buckets"
            2. Scatter - go over input array putting each item in a bucket
            3. Sort each non empty bucket
            4. Gather - visit buckets in order and put elements back into original array


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

Note: number of buckets matters, i'll just use 10 as an example
- can be used with hash fn to distribute elements into buckets
"""

def bucket_sort(arr):
    max_val = max(arr)
    # create buckets
    n = 10                                      # n = number of buckets
    buckets = [[]*n]                            # array of 10 buckets
    # put things from the input into the bucket
    for i in range(len(arr)):
        buckets[arr[i]//n].append(arr[i])

    for index, bucket in enumerate(buckets):    # enumerate returns an index and value



