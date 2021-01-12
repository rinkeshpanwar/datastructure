import time
import os
import psutil
pid = os.getpid()
py = psutil.Process(pid)
start = time.time()
s = {None}
for i in range(1000000):
    s.add(i)
print("set time taken->",time.time()-start)
start = time.time()
d = {}
for i in range(1000000):
    d[i]=True
print("Insertion time taken in dictionary->",time.time()-start)
start = time.time()
l = []
for i in range(1000000):
    l.append(i)
print("List time taken for insertion",time.time()-start)
start = time.time()
for i in s:
    if 1000000 == i:
        break
1000000 in s
print("Lookup time in set->",time.time()-start)
start = time.time()
for i in d:
    if 1000000 == i:
        break
1000000 in d
print("lookup time in dict->",time.time()-start)
start = time.time()
for i in l:
    if 1000000 == i:
        break
1000000 in l
print("lookup time in list->",time.time()-start)
start = time.time()
cs = set(l)
1000000 in cs
print("conversion from list to set and lookup time",time.time()-start)
memory = py.memory_info()[0]/2.**30
print("memory usage->",memory)