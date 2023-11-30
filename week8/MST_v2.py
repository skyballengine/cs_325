"""
Implement Prims’ algorithm Name your function Prims(G). Include function in the file MST.PY. You can either use brute force approach or priority queue. Try to see if you can come up with a solution using priority queue.
Input: a graph represented as an adjacency matrix
For example, the graph in the Exploration would be represented as the below (where index 0 is A, index 1 is B, etc.).
input = [
[0, 8, 5, 0, 0, 0, 0],
[8, 0, 10, 2, 18, 0, 0],
[5, 10, 0, 3, 0, 16, 0],
[0, 2, 3, 0, 12, 30, 14],
[0, 18, 0, 12, 0, 0, 4],
[0, 0, 16, 30, 0, 0, 26],
[0, 0, 0, 14, 4, 26, 0]
]
Output: a list of tuples, wherein each tuple represents an edge of the MST as (v1, v2, weight)
For example, the MST of the graph in the Exploration would be represented as the below.
output = [(0, 2, 5), (2, 3, 3), (3, 1, 2), (3, 4, 12), (2, 5, 16), (4, 6, 4)]
Note: the order of edge tuples within the output does not matter; additionally, the order of vertices within each edge does not matter. For example, another valid
output would be below (v1 and v2 in the first edge are flip-flopped; the last two edges in the list are flip-flopped).
output = [(2, 0, 5), (2, 3, 3), (3, 1, 2), (3, 4, 12), (4, 6, 4), (2, 5, 16)]
"""
import heapq


def Prims(G):
    # create priority queue
    pq = []
    # use first vertex in adjacency matrix as source
    source = 0
    mst = []
    # create dicts for distance
    # and for previous which is visited
    distance = dict()
    visited = [source]
    # iterate through the vertices of G; first
    for v in range(len(G)):
        distance[v] = 1000


    # initialize source as 0 and
    distance[source] = 0

    for k in range(1, len(G[0])):
        if 0 < G[0][k] < distance[k]:
            heapq.heappush(pq, (G[0][k], 0, k))
    weight, source, dest = heapq.heappop(pq)
    distance[dest] = weight
    mst.append((weight, source, dest))


    # iterate through the neighboring nodes on the adjacency matrix
    # current = source
    # i is the vertex of G (index)
    for i in range(1, len(G)):
        # j is the vertex (index) and the weight is the value of current[i][j]
        for j in range(len(G[i])):
            if 0 < G[i][j] < distance[i]:
                distance[i] = G[i][j]
                if i in visited and j not in visited:
                    heapq.heappush(pq, (G[i][j], i, j))
        if pq:
            weight, source, dest = heapq.heappop(pq)
            visited.append(source)
            mst.append((weight, source, dest))

    return mst


graph = [
    [0, 8, 5, 0, 0, 0, 0],
    [8, 0, 10, 2, 18, 0, 0],
    [5, 10, 0, 3, 0, 16, 0],
    [0, 2, 3, 0, 12, 30, 14],
    [0, 18, 0, 12, 0, 0, 4],
    [0, 0, 16, 30, 0, 0, 26],
    [0, 0, 0, 14, 4, 26, 0]
]

print(Prims(graph))
