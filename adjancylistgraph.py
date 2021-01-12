class graph:
    def __init__(self):
        self.graph_adjancy = {}
    
    def add_edge(self,u,v):
        if u not in self.graph_adjancy.keys():
            self.graph_adjancy[u]=[v]
        else:
            self.graph_adjancy[u].append(v)
        if v not in self.graph_adjancy.keys():
            self.graph_adjancy[v]=[u]
        else:
            self.graph_adjancy[v].append(u)
        
        return
    
    def printGraph(self):
        print(self.graph_adjancy)
        return
    
    def dfs(self,start,visited):
        print(start,end=' ')
        visited.add(start)
        for i in self.graph_adjancy[start]:
            if i not in visited:
                self.dfs(i,visited)
g = graph()
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(8,3)
g.add_edge(0,4)
g.printGraph()
visited = set()
g.dfs(4,visited)
print(visited)