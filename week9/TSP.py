from copy import deepcopy

def solve_tsp(G):
    # create deep copy of G
    g_copy = deepcopy(G)
    # establish source
    source = 0
    curr = source
    # empty cycle list
    cycle = [curr]
    # dummy value
    distance = [True]
    # main loop
    while distance:
        distance = [weight for index, weight in enumerate(G[curr]) if weight != 0 and index not in cycle]
        if distance:
            min_distance = min(distance)
            if G[curr].index(min_distance) not in cycle:
                next_vertex = G[curr].index(min_distance)
                cycle.append(next_vertex)

            else:
                index = G[curr].index(min_distance)
                g_copy[curr][index] = 0
                next_vertex = g_copy[curr].index(min_distance)
                cycle.append(next_vertex)

            curr = next_vertex
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