def solve_puzzle(Board, Source, Destination):
    # define lengths n and m
    n = len(Board)
    m = len(Board[0])
    directions = ""
    # a 2d matrix stating which coordinates (vertexes) have been visited so far (
    # Note: if a vertex is an obstacle, it is defined as True (visited)because we can't go there

    # possible moves: up, down, right, left
    adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    moves_dict = dict()
    # stack is initialized with source coordinates

    # path that will be the answer
    # after each move, we append the vertex to g_path
    visited = dict()
    # create a legal moves dict, each key has a list of values from adjacents
    for a in range(n):
        for b in range(m):
            moves_dict[(a, b)] = []
            # building legal_moves dict
            for i, j in adjacents:
                if 0 <= a + i < n and 0 <= b + j < m and Board[a + i][b + j] != 'Blocked':
                    moves_dict[(a, b)] += [(a + i, b + j)]
            # building visited dict
            visited[(a, b)] = False if Board[a][b] == '-' else True

    # dict_print = [print(k, v) for k, v in moves_dict.items()]
    visited[Source] = True
    # SO FAR SO GOOD
    queue = [(Source, [Source])]
    # visited = {Source}
    while queue:
        curr, path = queue.pop(0)
        if curr == Destination:
            return path
        for v in moves_dict[curr]:
            if not visited[v]:
                queue.append((v, path + [v]))
                # directions += get_direction(v, curr)
                visited[v] = True
    return None


def get_direction(current, previous):
    x = current[0] - previous[0]
    y = current[1] - previous[1]
    coordinate = (x, y)
    match coordinate:
        case (0, 1):
            return 'R'
        case (0, -1):
            return 'L'
        case (1, 0):
            return 'D'
        case (-1, 0):
            return 'U'




Puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]
print(solve_puzzle(Puzzle, (0, 0), (4, 4)))
