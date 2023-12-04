''' 
WRITE YOUR CODE FOR printVertexCover in below code
'''
from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation 
class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printVertexCover(self):
        solution = {}
        edges = [(key, value) for key in self.graph.keys() for value in self.graph[key]]
        print(edges)
''' 
WRITE YOUR CODE FOR printVertexCover
approx-vertex-cover(G):
    solution = {}
    Edges = All edges in G
    while(Edges is not empty):
        pick arbitrary edge E whose vertices are (u,v)
        solution = union(solution, {u,v})
        remove all edges that are connected to either u or v

    return solution
'''




# Create a graph given in
g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(5, 6)

g.printVertexCover()