"""
@author: David Lei
@since: 21/08/2016
@modified:

How it works: at each stage, divide the problem around a pivot into 2 partitions. One containing things less than the
                pivot and another containing things greater or eqal to the pivot. Note that the paritioned lists will not
                include the pivot. This will keep on going until the list is of len 1 and then we can just put the overall
                list back together.

Invariants: section < pivot | pivot | section >= pivot

Compared to merge: work is done in the splitting of the array

Time complexity
- best O(n log n), when a decent pviot is chose for around event splitting
- worst O(n^2), when the pviot only discards one element from the array each time, thus needs to do it N^2 times
- avg O(n log n)

Space complexity
- O(N), create new lists when we split? and combine back up? so 2N = O(N)?
- O(log n), when you recur on the smaller list and use tail recursion to optimize 

Stability: Not stable

"""
count = 0

def quick_sort(arr):
    """
    This works and uses the idea of quick sort but it can be done in place of the one array instead of making a new
    array which takes space
    """
    global count
    count += 1
    print(count)

    if len(arr) <= 1:
        return arr
    else:
        # assume last item chosen as pivot
        pivot = arr[-1]

        wall = 0                        # everything before wall is < pivot
        for i in range(len(arr)-1):     # last element is pivot
            if arr[i] < pivot:
                temp = arr[wall]        # less than pivot
                arr[wall] = arr[i]      # move to index wall (everything before it will be <)
                arr[i] = temp
                wall += 1               # increment wall (so arr[i] is < pivot, now it is behind the wall)
        arr[len(arr)-1] = arr[wall]     # swap pivot with first element !< pivot
        arr[wall] = pivot

        less_than = quick_sort(arr[:wall])
        greater_eq_than = quick_sort(arr[wall+1:])

        return less_than + arr[wall:wall+1] + greater_eq_than

if __name__ == "__main___":

    arr = [1,2,3,4]
    bar = [8, 100 ,1,-3,11,1,0]
    car = [0,-3,1,-2]
    foo = [123,91,-19, 1,1,2,1,-54,1909,-51293,192,3,-4]
    print(quick_sort(foo))