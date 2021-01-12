def checkSorted(arr):
    s = sorted(arr)
    for i in range(len(arr)):
        if arr[i]!=s[i]:
            break
    return len(arr)-i
arr = [1,2,6,2,4,5]
print(checkSorted(arr))