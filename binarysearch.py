def binary_Search(low,high,arr,data):
    #go until condition true low<=high
    while low<=high:
        #calculate mid value
        mid = high + low //2
        #check if mid value is your data
        if data == arr[mid]:
            return mid
        #chech whether data is greater than mid the add 1 to mid and made it low
        if data > arr[mid]:
            low = mid +1
        #else make hig mid -1
        if data < arr[mid]:
            high = mid -1
    #if value is not found return -1
    return-1

arr = [5,8,6,9,2,5]
arr.sort()
low = 0
high = len(arr)-1
data = 6
print(high)
print(binary_Search(low,high,arr,data))