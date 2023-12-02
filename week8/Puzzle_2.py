"""
You are given a 2-D puzzle of size MxN, that has N rows and M column (M and N can be different).
Each cell in the puzzle is either empty or has a barrier.
An empty cell is marked by ‘-’ (hyphen) and the one with a barrier is marked by ‘#’.
You are given two coordinates from the puzzle (a,b) and (x,y). You are currently located at (a,b) and want to reach (x,y).

You can move only in the following directions:
L: move to left cell from the current cell
R: move to right cell from the current cell
U: move to upper cell from the current cell
D: move to the lower cell from the current cell

Input: board, source, destination

board: is puzzle as below:
source: A tuple representing the indices of the starting position, e.g. for the upper right corner, source=(0, 4).
destination: A tuple representing the indices of the goal position, e.g. for the lower right corner, goal=(4, 4).

Puzzle: A list of lists, each list represents a row in the rectangular puzzle.
Each element is either ‘-’ for empty (passable) or ‘#’ for obstacle (impassable).
Puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]
"""

"""

"""
# import heapq
def solve_puzzle(Board, Source, Destination):
    # define lengths n and m
    n = len(Board)
    m = len(Board[0])
    # starting coordinates
    source_x, source_y = Source
    # destination coordinates
    destination_x, destination_y = Destination

    # a 2d matrix stating which coordinates (vertexes) have been visited so far (
    # Note: if a vertex is an obstacle, it is defined as True (visited)because we can't go there
    # visited = [([False] if Board[i][j] == '-' else ['Blocked']) for i in range(n) for j in range(m)]
    visited = dict()
    # print(visited)

    # possible moves: up, down, right, left
    adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    moves_dict = dict()
    # stack is initialized with source coordinates
    stack = [Source]

    # path that will be the answer
    # after each move, we append the vertex to g_path
    results_list = []

    # create a legal moves dict, each key has a list of values from adjacents
    for a in range(n):
        for b in range(m):
            moves_dict[(a, b)] = []
            # building legal_moves dict
            for i, j in adjacents:
                if 0 <= a + i < n and 0 <= b + j < m and Board[a+i][b+j] != 'Blocked':
                    moves_dict[(a, b)] += [(a+i, b+j)]
            # building visited dict
            visited[(a, b)] = False if Board[a][b] == '-' else True

    # dict_print = [print(k, v) for k, v in moves_dict.items()]
    # SO FAR SO GOOD
    # ------------------------------------------



    # print(moves_dict)
    for current in moves_dict[Source]:
        if not visited[current]:
            puzzle_helper(Board, current, Destination, visited, moves_dict, stack)
            # print(f"stack: {stack}")
        results_list.append(stack)
        # print(f"results_list: {results_list}")
    # find the minimum length list and return that list
    return results_list


def puzzle_helper(board, current, dest, visited, moves_dict, stack):
    # print(current, dest)
    if current == dest:
        visited[current] = True
        stack.append(current)
        return

    visited[current] = True
    stack.append(current)
    for pos in moves_dict[current]:
        if not visited[pos]:
            # stack.append(pos)
            puzzle_helper(board, pos, dest, visited, moves_dict, stack)
            return stack



Puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]
print(solve_puzzle(Puzzle, (0, 0), (4, 4)))

