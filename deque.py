import collections

dq = collections.deque()
dq.append(10)
dq.append(20)
dq.append(30)
print(dq)
dq.appendleft(100)
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)

print("dequeue important function")
de = collections.deque([1, 2, 3, 3, 4, 2, 4]) 
print ("The number 4 first occurs at a position : ") 
print (de.index(4,2,5)) 
de.insert(4,3) 
print ("The deque after inserting 3 at 5th position is : ") 
print (de) 
print ("The count of 3 in deque is : ") 
print (de.count(5))

