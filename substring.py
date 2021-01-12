def subStrinng(s1,s2,i,j,c):
    if i<0 and j>-1:
        return False
    elif j<0:
        return True
    elif s1[i] == s2[j]:
        return subStrinng(s1,s2,i-1,j-1,1)
    elif c == 1:
        return subStrinng(s1,s2,i,len(s2)-1,0)
    else:
        return subStrinng(s1,s2,i-1,len(s2)-1,0)
a = 'AAABABA'
b = 'AABA'
print(subStrinng(a,b,len(a)-1,len(b)-1,0))