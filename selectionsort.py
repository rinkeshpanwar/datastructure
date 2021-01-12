''' 
suppose we are having a array
[10,5,7,20,40]
take first index and check for lowest value in array such that value>index
5 is the smallest one so swap them
[5,10,7,20,40]
now go to index 2 and check which are the smallest value i array such that value[index]>index
7 is smallest so swap them
[5,7,10,20,40]
go until you didnt reach at n-1 index since last index will be highest value
'''


def sortlist(li):
    for i in range(len(li)):
        if li[i] > min(li[i:]):
            swap_value = li[li.index(min(li[i:]))]
            swap_index = li.index(min(li[i:]))
            temp = li[i]
            li[i] = swap_value
            li[swap_index] = temp
    return li
print(sortlist([23,89,90,96,897,12,0,1,-1,-234]))


'''
Another way to do is 
A = [64, 25, 12, 22, 11] 
  
# Traverse through all array elements 
for i in range(len(A)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i] 
  
# Driver code to test above 
print ("Sorted array") 
for i in range(len(A)): 
    print("%d" %A[i]),  
'''