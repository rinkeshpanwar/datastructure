# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import copy
def flipMatrix(A,i,j):
    if (i >= len(A)):
        return 
    if (A[i][j]==0):
        A[i][j] =1
    if (A[i][j]==1):
        A[i][j] =0
    flipMatrix(A,i+1,j)

def solution(c):
    row = len(c)
    col = len(c[0])
    max = 0
    
    for k in range(col):
        A = copy.copy(c)
        for i in range(row):
            for j in range(0,col):
                if 0!=k:
                    flipMatrix(A,i,j)
        count = 0   
        for i in range(len(A)):
            temp = True
            for  j in range(len(A[0])):
                if A[i][j]!=A[i][0] :
                    temp = False
            if temp == True:
                count+=1
        
        if count > max:
            max = count
    return max
    pass

print(solution([[0, 0, 0, 0], [0, 1, 0, 0], [1, 0, 1, 1]]))