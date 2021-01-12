def lcs(i,s1,j,s2):
    if i < 0 or j < 0:
        return 0
    elif s1[i]==s2[j]:
        return 1+lcs(i-1,s1,j-1,s2)
    else:
        return max(lcs(i-1,s1,j,s2),lcs(i,s1,j-1,s2))

s1 ='badabda'
s2 = 'dabdabadab'
print(lcs(len(s1)-1,s1,len(s2)-1,s2))