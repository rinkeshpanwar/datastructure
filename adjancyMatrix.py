class graph:
        def __init__(self,v):
            self.graph = []
            for i in range(v):
                self.graph.append([0 for j in range(v)])      

        def addEdge(self,u,v):
            if self.graph[u][v]==1:
                print("Element is already present in list")
                return
            self.graph[u][v]=1
            self.graph[v][u]=1
            return

g = graph(5)
g.addEdge(0,0)
g.addEdge(3,2)
print(g.graph)