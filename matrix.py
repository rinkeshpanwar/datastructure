# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def flipMatrix(A,i,j):
    if (i >= len(A)):
        return 
    if (A[i][j]==0):
        A[i][j] =1
    if (A[i][j]==1):
        A[i][j] =0
    flipMatrix(A,i+1,j)

def solution(A):
    row = len(A)
    col = len(A[0])
    for i in range(row):
        flip = A[i][0]
        for j in range(1,col):
            if A[i][j]!=flip:
                flipMatrix(A,i,j)
    count = 0   
    for i in range(len(A)):
        temp = True
        for  j in range(len(A[0])):
            if A[i][j]!=A[i][0]:
                temp = False
        if temp == True:
            count+=1
    return count
    pass
