
def knapsack(weight,profit):
    bag = 94
    ptr = len(weight)-1
    totalProfit = 0
    while(bag!=0 and ptr>=0):
        if (bag>=weight[ptr]):
            totalProfit+=profit[ptr]
            bag-=weight[ptr]
        else:
            ptr-=1
    return totalProfit

weight = [1,2,3,4,5]
profit = [10,20,30,40,50]
print(knapsack(weight,profit))