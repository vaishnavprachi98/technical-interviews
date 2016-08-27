"""
@author: David Lei
@since: 27/08/2016
@modified: 

"""
from collections import deque
# double linked list (can act as a stack, queue, linked list etc)
stack = deque()

n = int(input())
arr = [int(x) for x in input().split(' ')]
result = [1 for _ in range(n//2)]
counter = 0

for i in range(len(arr)):
    if len(stack) > 0:

        top = stack.pop()
        if arr[top[0]-1] == arr[i]:
            # closing to an open bracket
            #counter -= 1
            if top[1] == i - 1:     # newer opening
                pass
            else:
                counter -= 1
            result[counter-1] = 0
            if counter == n//2:
                counter -= 1

            #print(counter)
            #print('closed')
        else:
            stack.append(top)
            info = arr[i], i
            stack.append(info)    # add a new opening
            if arr[i] < i:
                # awkward closing
                pass
            else:
                # new opening
                counter += 1
        print(stack)

    else:
        info = arr[i], i
        stack.append(info)        # add a new opening
        counter += 1
    print(stack)
print(result)

"""
8
8 7 4 3 6 5 2 1

8
3 8 1 5 4 7 6 2

8
3 5 1 7 2 8 4 6

8
5 3 2 7 1 8 4 6

8
8 7 5 6 3 4 2 1
"""