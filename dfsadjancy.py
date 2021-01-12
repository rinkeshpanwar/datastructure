class graph:
    def __init__(self,v):
        self.v = v
        self.adj_graph = [[0 for j in range(v)] for i in range(v)]
    
    def printgraph(self):
        print(self.adj_graph)
        return
    
    def addEdge(self,u,v):
        self.adj_graph[u][v] = 1
        self.adj_graph[v][u] = 1

    def dfs(self,start,visited):
        print(start,end=' ')
        visited[start] = True
        for i in range(self.v):
            if (self.adj_graph[start][i]==1) and (not visited[i]):
                self.dfs(i,visited)
    
g = graph(4)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,1)
g.addEdge(1,0)
#g.printgraph()
visited = [False]*4
print(visited)
g.dfs(3,visited)
print(visited)