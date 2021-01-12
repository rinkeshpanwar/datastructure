import time
start = time.time()
a = [1,2,3,4,5,6,7,8,9,10,31,32,33,34,35,36,337]
b = [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,337,338]
p1=p2=0
k =[]
an = len(a)-1
bn = len(b)-1
#merging of two array
while(p1<=an and p2<=bn):
	if a[p1]<b[p2]:
		k.append(a[p1])
		p1+=1
	elif b[p2]<a[p1]:
		k.append(b[p2])
		p2+=1
	else:
		k.append(b[p2])
		k.append(a[p1])
		p2+=1
		p1+=1
if p1>an and p2<=bn:
	for i in range(p2,bn+1):
		k.append(b[i])
elif p2>bn and p1<=an:
	for i in range(p1,an):
		k.append(a[i])
print(time.time()-start)
print(k)