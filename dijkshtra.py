def minValue(dset,value):
    highest = 1000
    kHighest = None
    for k,v in value.items():
        if v <highest and k not in dset:
            kHighest = k
            highest = v
    return kHighest  


def dij(g):
    dset = set()
    value = {0:0}
    parent = {0:-1}
    for i in range(len(g[0])):
        if i!=0:
            value[i] = 1000
            parent[i] = None
    for i in range(len(g[0])):
        u = minValue(dset,value)
        #print(u)
        dset.add(u)
        for j in range(len(g[0])):
            if (g[u][j]!=0) and (j not in dset) and (value[u]+g[u][j] < value[j]):
                value[j] = value[u]+g[u][j]
                parent[j] = u
                
    

g = [[0,0,0,0,1,7],
    [0,0,1,6,0,0],
    [0,1,0,2,4,0],
    [0,6,2,0,3,6],
    [1,0,4,3,5,0],
    [7,0,0,6,5,0]]
dij(g)