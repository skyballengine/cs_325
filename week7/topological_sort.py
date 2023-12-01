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

    def add_edge(self, u, v):
        self.graph[u].append(v)

def topological_sort(input_graph):
    stack = []  # results begins as empty

    visited = [False] * input_graph.vertices    # define visited array

    # for each node in the graph
    for curr_node in range(input_graph.vertices):
        print(f"top_sort: {stack}")
        print(f"top_sort: {curr_node}")
        # if not visited, then pass to the helper function
        if not visited[curr_node]:
            helper_topological_sort(input_graph, curr_node, visited, stack)

    return stack

# Helper function that marks node as visited, then checks all adjacent nodes
def helper_topological_sort(input_graph, node, visited, results):
    print(f"helper: {results}")
    print(f"helper: {node}")
    visited[node] = True    # mark current node as visited

    # recur for all adjacent vertices
    for i in input_graph.graph[node]:
        if not visited[i]:
            helper_topological_sort(input_graph, i, visited, results)
    results.insert(0, node)



my_graph = Graph(5)
my_graph_2 = Graph(10)
my_graph.add_edge(0, 1)
my_graph.add_edge(0, 3)
my_graph.add_edge(1, 2)
my_graph.add_edge(2, 3)
my_graph.add_edge(2, 4)
my_graph.add_edge(3, 4)
print(my_graph.graph)
print(my_graph_2.graph)

print("Topological Sort")
 print(topological_sort(my_graph))

