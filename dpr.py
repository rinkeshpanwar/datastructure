def ml(i,arr):
    if i<0:
        return 0
    a = ml(i-1,arr)+arr[i]
    return max(arr[i],a)


arr = [10,0,20,10,-100,-1,1,101]
m = 0
for i in range(len(arr)):
    m = max(m,ml(i,arr))
print(m)
