class solution:
    def __init__(self):
        self.sum = 0
        self.permu = 1
    def sumValue(self,n):
        if n==0:
            return
        self.sumValue(n-1)
        self.sum+=n
        print(self.sum)
    def permutation(self,n):
        if n ==0:
            return
        self.permu*=n
        print(self.permu)
        self.permutation(n-1)

obj = solution()
#obj.sumValue(5)
obj.permutation(5)