def maxSubArray(arr,i):
    if i <0:
        return 0
    c = maxSubArray(arr,i-1)
    return max(arr[i],c,c+arr[i])

arr = [-100,100,-100]
print(maxSubArray(arr,len(arr)-1))