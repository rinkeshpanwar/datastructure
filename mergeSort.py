import time
start = time.time()
def mergeSort(a):
    if len(a)==1:
        return a
    low = 0
    high = len(a)-1
    mid = (low+high)//2
    return merge(mergeSort(a[low:mid+1]),mergeSort(a[mid+1:high+1]))

def merge(a,b):
    temp =[]
    if len(a)<1 and len(b)<1:return
    la = len(a)-1
    lb = len(b)-1
    p1=p2=0
    while(p1<=la and p2<=lb):
        if a[p1]<b[p2]:
            temp.append(a[p1])
            p1+=1
        elif b[p2]<a[p1]:
            temp.append(b[p2])
            p2+=1
        else:
            temp.append(a[p1])
            temp.append(b[p2])
            p1+=1
            p2+=1
    if p1>la and p2<=lb:
        for i in range(p2,lb+1):
            temp.append(b[i])
    elif p2>lb and p1<=la:
        for i in range(p1,la+1):
            temp.append(a[i])
    return temp


a = [1]
b = [10,8,4,12,65,23,45,65,32,21,234,56,67,54,32,22,34,21,29,27,21,10,9,4]
#print(merge(a,b))
print(mergeSort(b))
print("time taken=",time.time()-start)