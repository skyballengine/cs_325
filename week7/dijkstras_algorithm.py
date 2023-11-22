"""
Implement a function calculate_distances(graph, starting_vertex)

Example: 
example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
calculate_distances(example_graph, 'X')

would return
{'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}
"""

from operator import itemgetter
import heapq


def calculate_distance(graph, starting_vertex):
    # # create a queue
    # queue = []
    # # iterate through, initializing the keys and inserting into queue
    # for v in graph.keys():
    #     queue.insert(0, [v, 10000])
    # # reset the priority of the starting_index to 0 to use first
    # i = queue.index((starting_vertex, 10000))
    # queue[i][1] = 0
    # # create a visited list
    # visited = {}
    # # main loop to move through queue of vertices and thus move through the graph
    # while len(queue) > 0:
    #     curr_node = min(queue, key=itemgetter(1))
    #     queue.remove(curr_node)
    #     # curr_node = queue.pop()
    #     visited[curr_node[0]] = curr_node[1]
    #     for v in graph[curr_node].keys():
    #         dist_v = min(curr_node[v], )

    # # create a distances table and an initial list of unvisited vertices
    # unvisited = []
    # distances = {}
    # # iterate through, initializing the keys and inserting into queue
    # for v in graph.keys():
    #     # initialize visited with large values
    #     unvisited.append(v)
    #     distances[v] = 1000
    # # reset starting_index to 0 to use first
    # distances[starting_vertex] = 0
    #
    # # main loop to move through vertices and thus move through the graph
    # while len(unvisited) > 0:
    #     # current node is the element with the lowest value it's 2nd element
    #     curr_node = min(graph, key=graph.get)
    #     min_val = graph[curr_node]
    #     unvisited.remove(curr_node)
    #     # curr_node = queue.pop()
    #     distances[curr_node] = min_val
    #     for v in graph[curr_node].keys():
    #         # need min of destination node distance vs current node distance + distance to next vertex
    #         distances[curr_node] = min(distances[curr_node], distances[curr_node] + graph[cu])
    pass


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        # pop current distance and current vertex from the priority queue (lowest value)
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.

        # if the current distance is greater than what we already have on file in the distances dict, then continue
        # we're only interested in values that are less than what we currently have recorded
        if current_distance > distances[current_vertex]:
            continue

        # unpack the key and value: neighbor (vertex) and weight (distance) of the adjacent vertices in the graph
        # dictionary
        for neighbor, weight in graph[current_vertex].items():
            # establish new distance that sums current distance and weight of the vertex
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                # update the dictionary entry
                distances[neighbor] = distance
                # push the new (distance, vertex) tuple onto the heap
                heapq.heappush(pq, (distance, neighbor))

    return distances


example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
print(calculate_distances(example_graph, 'X'))
# => {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}

'''
Reference:
source: https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
'''
