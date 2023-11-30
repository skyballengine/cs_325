import heapq

def Prims(G):
    num_vertices = len(G)
    visited = [False] * num_vertices
    pq = []
    pq.append((0, 0, None))
    mst = []

    while pq:
        w, curr, prev = heapq.heappop(pq)
        if visited[curr]:
            continue

        visited[curr] = True

        if prev is not None:
            mst.append((w, curr, prev))

        for v in range(len(G)):
            if G[curr][v] != 0 and not visited[v]:
                heapq.heappush(pq, (G[curr][v], v, curr))

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