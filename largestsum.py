
a =[-1,2,3,-4,5,6,-111,-999]
maxSoFar = 0
localMax = 0
for i in range(len(a)):
    localMax+=a[i]
    if localMax > maxSoFar:
        maxSoFar = localMax
    if localMax < 0:
        localMax = 0

print(maxSoFar)