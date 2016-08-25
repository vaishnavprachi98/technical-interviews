import math

coinDenom = [1,3,5,6,8]
val = 7

m = [math.inf]*(val+1)
m[0] = 0


for coin in coinDenom:
    for i in range(len(m)):
        if i >= coin:
            m[i] = min(m[i], m[i-coin]+1)

if m[val] == math.inf:
    for i in range(val,-1,-1):
        if m[i] != math.inf():
            m[val] = m[i]
            break

print(m)
