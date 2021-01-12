def perItemProfit(weight,profit):
    profitPerKg = []
    for i in range(0,len(weight)):
        profitPerKg.append(profit[i]/weight[i])
    return profitPerKg

def sortThreeList(weight,profit,profitPerItem):
    for i in range(0,len(weight)-1):
        #sorting on selectionsort Algorithm
        tempIndex = profitPerItem.index(max(profitPerItem[i+1:]))
        if (profitPerItem[i]<profitPerItem[tempIndex]):
            tempValue = profitPerItem[i]
            profitPerItem[i] = profitPerItem[tempIndex]
            profitPerItem[tempIndex] = tempValue
            #swapping index for weight
            tempValue = weight[i]
            weight[i] = weight[tempIndex]
            weight[tempIndex] = tempValue
            #swapping for profit
            tempValue = profit[i]
            profit[i] = profit[tempIndex]
            profit[tempIndex] = tempValue

def fractionalKnapsack(weight,profit,bagCapacity):
    totalProfit = 0.0
    profitPerItem = perItemProfit(weight,profit)
    #in python it is always pass by reference so value will be updated inside the function so no need of assignment
    sortThreeList(weight,profit,profitPerItem)
    ptr = 0
    print(weight)
    print(profit)
    print(profitPerItem)
    while(ptr!=len(weight) and bagCapacity!=0):
        if weight[ptr]<=bagCapacity:
            totalProfit+=profitPerItem[ptr]*weight[ptr]
            bagCapacity-=weight[ptr]
        elif bagCapacity<weight[ptr] and bagCapacity!=0:
            totalProfit+=profitPerItem[ptr]*bagCapacity
            bagCapacity-=weight[ptr]-bagCapacity
        else:
            ptr+=1
    return totalProfit

weight = [1,2,3]
profit = [4,5,6]
bagCapacity = 5
print(fractionalKnapsack(weight,profit,bagCapacity))