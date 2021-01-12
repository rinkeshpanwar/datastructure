def createMatrix(n):
    matrix = []
    count = 0
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(count)
            count+=1
        matrix.append(temp)
    return matrix

def isDanger(matrix,i,j,n):
    if i < 0 or i >=n or j < 0 or j>=n:
        return True
    return False

def roverPosition(matrix,n,position):
    i = 0
    j = 0
    for p in position:
        if p=='LEFT' and not isDanger(matrix,i,j-1,n):
            j-=1
        elif p=='RIGHT' and not isDanger(matrix,i,j+1,n):
            j+=1
        elif p=='UP' and not isDanger(matrix,i-1,j,n):
            i-=1
        elif p=='DOWN' and not isDanger(matrix,i+1,j,n):
            i+=1
        else:
            continue
    return matrix[i][j]

n = 6
position = ['RIGHT','LEFT','LEFT','RIGHT','RIGHT']
matrix = createMatrix(n)
print(roverPosition(matrix,n,position))
