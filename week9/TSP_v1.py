"""
Implement Travelling Salesman Problem using the nearest-neighbor heuristic.
Input: The input Graph is provided in the form of a 2-D matrix (adjacency matrix). Consider the first node as the starting point.
Sample input:
G = [
[0, 2, 3, 20, 1],
[2, 0, 15, 2, 20],
[3, 15, 0, 20, 13],
[20, 2, 20, 0, 9],
[1, 20, 13, 9, 0],
]
Output: A list of indices indicating the path taken. You must return the sequence of nodes, the path taken starting from node 0. In this example, G is 5x5, indicating there are 5 nodes in this graph: 0-4. You will always begin with node 0, and your
path should include every node exactly once, and only go between nodes with a
nonzero edge between them. You path will end at the starting node.
Sample output (For above graph G):
[0, 4, 3, 1, 2, 0]
Note: Not all graphs are fully connected: some rows in G may have more than one 0.
These indicate absence of an edge.
"""


def solve_tsp(G):
    # create source
    source = 0
    # create visited list
    # create cycle list
    cycle = [source]
    # navigate adjacency matrix using nearest neighbor heuristic
    for i in range(len(G)):
        distance = [weight for index, weight in enumerate(G[i]) if weight != 0 and index not in cycle]
        # print(distance)
        if distance:
            print(distance)
            min_distance = min(distance)
            print(min_distance)
            vertex = G[i].index(min_distance)
            print(vertex)
            if vertex not in cycle:
                cycle.append(vertex)
            else:
                new_vertex = G[i][vertex + 1:].index(min_distance)
                vertex = new_vertex + (vertex + 1)
                cycle.append(vertex)
    cycle.append(source)
    return cycle

print(solve_tsp([
    [0, 2, 3, 20, 0],
    [2, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [20, 2, 20, 0, 9],
    [0, 20, 13, 9, 0],
]))

print(solve_tsp([
    [0, 2, 3, 20, 1],
    [2, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [20, 2, 20, 0, 9],
    [1, 20, 13, 9, 0],
]))

print(solve_tsp([]))
