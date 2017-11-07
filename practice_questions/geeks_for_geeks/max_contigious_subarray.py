"""
@author: David Lei
@since: 7/11/2017

http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

"""
def max_subarray_sum(array):
    max_so_far = array[0]
    current_max = array[0]
    for i in range(1, len(array)):
        # Best we can do is either best we can do previously + new item,
        # or just new item is best we can do prev was negative.
        current_max = max(array[i], current_max + array[i])
        max_so_far = max(max_so_far, current_max)
    return max_so_far

print(max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]))  # 7.


# Extension: http://www.geeksforgeeks.org/largest-sum-subarray-least-k-numbers/
# Largest sum subarray with at k items, question is for at least k numbers, I did k numbers because idk.

def max_k_subarray_sum(array, k): # O(n)
    max_so_far = array[0]
    current_max = array[0]
    cumulative_max = [max_so_far]
    for i in range(1, len(array)):
        # Best we can do is either best we can do previously + new item,
        # or just new item is best we can do prev was negative.
        current_max = max(array[i], current_max + array[i])
        cumulative_max.append(current_max)

    sum_so_far = sum(array[:k])
    current_k_max = sum_so_far

    for i in range(k, len(array)):
        sum_so_far -= array[i - k]
        sum_so_far += array[i]
        # print("- %s, + %s, sum: %s" % (array[i - k - 1], array[i], sum_so_far))
        current_k_max = max(sum_so_far, current_k_max)

    return current_k_max

print(max_k_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3], 3))  # 4.
