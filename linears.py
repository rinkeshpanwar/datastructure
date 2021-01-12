def linear(l,srh):
    counter =0
    for i in l:
        counter +=1
        if srh == i:
            return counter
    

a=[1,2,3,4,5,6,7]
print("found index at"+str(linear(a,5)))