"""
Implement a function topologicalSort(myGraph)

Example: 

# Create a graph 
myGraph = g.Graph(5)
myGraph.addEdge(0, 1)
myGraph.addEdge(0, 3)
myGraph.addEdge(1, 2)
myGraph.addEdge(2, 3)
myGraph.addEdge(2, 4)
myGraph.addEdge(3, 4)

topologicalSort(myGraph)

would return

[0, 1, 2, 3, 4]

"""

from collections import defaultdict


class Graph:
    # Constructor
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def topological_sort(self, graph):


my_graph = Graph(5)
my_graph_2 = Graph(10)
my_graph.addEdge(0, 1)
my_graph.addEdge(0, 3)
my_graph.addEdge(1, 2)
my_graph.addEdge(2, 3)
my_graph.addEdge(2, 4)
my_graph.addEdge(3, 4)
print(my_graph.graph)
print(my_graph_2.graph)
