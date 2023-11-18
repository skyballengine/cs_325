"""
Pseudocode:
Initialize an empty stack for storage of nodes, S.
For each vertex u, define u.visited to be false.
Push the root (first node to be visited) onto S.
While S is not empty:
    Pop the first element in S, u.
    If u.visited = false, then:
        U.visited = true
        for each unvisited neighbor w of u:
            Push w into S.
End process when all nodes have been visited.
"""

# No recursion
def depth_first_search(graph):
    # initalize set - visited and stack - list with graph root node as only element
    visited, stack = set(), [graph.root]
    # while stack is not empty, do the following
    while stack:
        print(stack)
        # remove last element from stack as current vertex
        vertex = stack.pop()
        # if current vertex is not in visited list
        if vertex not in visited:
            # add vertex to visited list
            visited.add(vertex)

            stack.extend(graph[vertex] - visited)
    return visited


# With Recursion
def depth_first_search_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        depth_first_search_recursive(graph, next, visited)
    return visited