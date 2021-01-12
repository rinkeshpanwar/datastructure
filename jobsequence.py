'''
given a profit and time for instance
profit = [10,20,5,15]
time = [2,1,3,1]
->we will sort profit in decreasing order so that the highest profit comes first. Here we will not sort value instead we will 
save sorted index value in new variable profitIndex and use it later for reference of highest profit later.
->Next we will find maximum time mxt which state that we can perform atmost mxt work, for this instance max value is 3 
.which means atmost 3 work can be done.
-> Now create 3 empty slot for work assign value -1. -1 means this slot is not yet occupied yet.
 _  ,_  ,_
-1  ,-1  ,-1
->now we will take profitIndex and start exploring profit as per profitIndex
index are [1,3,0,2]
profit are[20,15,10,5]
time      [1,1,2,3]
now take first index and find out its time which is 1 check for slot if 1 slot is empty or not
        -1,-1,-1 yes it is empty assign profit  value
        20,-1,-1
go for second value in index which is 3 and its corresponding
profit is  15  now check for time which is 1 which means it must be done withing 1 hour
check for first slot is it free?
    20,-1,-1 ---->slots
    no it is not free so not possible so we cannot assign it go for next index
index value 0 to be taken and its value for profit is 10 and its time is 2 so check for 2nd slot is it free if it is free assign 
profit to this slot if it is not free then go for below slot and check if it is not free also then go on until you reach free slot 
and first index. If there is no then this job cannot be done.
    in this case slot are
        20,-1,-1 yes slot is free so assign a profit
        20,10,-1
now do for same next index 2 profit is 5 and time taken is 3 so yes 3rd slot is free and we can assign value to it
    20,10,-1 yes free slot is available at index 2 so assign value to it
    20,10,5
->now all slot are occupied with some value so add all of them and return them..In this instance we have taken -1 for empty slot that
wil create some problem so better to take 0 so that if there is still empty slot then addidng them those dont create problem

'''
#python is passbyreference by default so we need to import copy for making copy of variable.
import copy
def profitIndexSort(profit):
    profitIndex = []
    profitCopy = copy.copy(profit)
    for i in range(len(profit)):
        temp = profitCopy.index(max(profitCopy))
        profitIndex.append(temp)
        profitCopy[temp]=-1
    return profitIndex

def checkEmptySlot(time,slot):
    for i in range(time-1,-1,-1):
        if slot[i]==0:
            return i
    return -1
def jobSequence(profit,time):
    totalProfit = 0
    jobsDone = []
    profitIndex = profitIndexSort(profit)
    #finding max time available
    mxt = max(time)
    #creating empty slot
    slot = [0 for i in range(mxt)]
    for i in profitIndex:
        #taking index value and check for empty slot if its free it will return index value ot it will return -1 for no empty slot
        indexValue = checkEmptySlot(time[i],slot)
        if indexValue !=-1:
            slot[indexValue]=profit[i]
            jobsDone.append(indexValue)
    for i in slot:
        totalProfit+=i
    jobsDone.reverse()
    print("JobsDone",jobsDone)
    return totalProfit

profit = [10,20,10,40,20,10]
time = [1,2,1,4,2,1]
print(jobSequence(profit,time))