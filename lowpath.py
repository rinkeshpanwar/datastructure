class a:
    total = 100000
    def findPath(self,g,i,j,temp):
        if i >2 or j>2 or i <0 or j <0:
            return
        if i==2 and j ==2 and temp+g[i][j]<self.total:
            self.total = temp+g[i][j]
        self.findPath(g,i,j+1,temp+g[i][j])
        self.findPath(g,i+1,j,temp+g[i][j])

g = [[1,2,3],[1,2,3],[1,2,3]]
o = a()
o.findPath(g,0,0,0)
print(o.total)