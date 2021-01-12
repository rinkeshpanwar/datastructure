class graph:
    def __init__(self,d):
        self.graph_dict = d

    def add(self,u,v):
        if u not in self.graph_dict.keys():
            self.graph_dict[u] = list(v)
            if v not in self.graph_dict.keys():
                self.graph_dict[v] = list(u)
            else:
                self.graph_dict[v].append(u)
            return
        self.graph_dict[u].append(v)
        self.graph_dict[v].append(u)
    def print_graph_vertex(self):
        print(self.graph_dict.keys())

    def print_whole_graph(self):
        print(self.graph_dict)
d = {"a":[],"b":[],"c":[],"d":[]}
g = graph(d)
g.add("a","d")
g.add("e","d")
g.add("h","a")
g.add("a","c")
#g.print_graph_vertex()
g.print_whole_graph()