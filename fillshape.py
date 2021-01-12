class shape:
    count = 0
    def fill_shape(self,fillShape,i,j):
        self.count+=1
        if i >4 or j>4 or fillShape[i][j]==1:
            return
        fillShape[i][j]=1
        self.fill_shape(fillShape,i,j+1)
        self.fill_shape(fillShape,i-1,j)
        self.fill_shape(fillShape,i+1,j)
        self.fill_shape(fillShape,i,j-1)

s = shape()
g = [[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1]]
s.fill_shape(g,2,3)
print(g,"count=",s.count)