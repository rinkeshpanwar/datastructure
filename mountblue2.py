def largestStar(star):
    maxStar = 0
    count = -1
    for i in star:
        if i == '|' and count<0:
            count+=1
        elif count>-1 and i=='|':
            maxStar = max(maxStar,count)
            count = 0
        elif count>-1:
            count+=1
        else:
            continue

    return maxStar

s = '|||||||||****|*****|**|*|'
print(largestStar(s))