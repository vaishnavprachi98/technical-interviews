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