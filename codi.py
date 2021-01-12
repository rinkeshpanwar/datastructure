def solution(A):
    maximumNumber = max(A)
    if maximumNumber < 1:
        return 1
    A.sort()
    temp = 0
    for i in range(len(A)):
        if A[i]>0:
            if A[i]-temp>1 :
                return temp+1
            temp = A[i]
    return len(A)+1
    pass

print(solution([i for i in range(101)]))