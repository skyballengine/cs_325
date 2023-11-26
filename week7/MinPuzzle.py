"""
Example
Input: puzzle[][] = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
Output: 1
Explanation: The minimal effort route would be [1, 2, 3, 4, 5] which has an effort of value 1.
This is better than other routes for instance, route [1, 3, 5, 3, 5] which has an effort of 2.
"""

import heapq


def minEffort(puzzle):
    # define dimensions of the puzzle 2d array
    m = len(puzzle)
    n = len(puzzle[0])
    # create range of move possibilities
    adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # create a 2d array of size m * n with large values that will be overwritten
    effort = [[1000] * n for j in range(m)]
    # change the value of the source cell to 0
    effort[0][0] = 0
    # create priority queue with the source cell
    pq = [(0, 0, 0)]
    # while loop that stops when pq is empty
    while len(pq) > 0:
        # print(effort)
        # print(pq)
        # pop lowest value from priority queue, best option
        current_m, current_n, current_effort = heapq.heappop(pq)
        # if the current effort is greater than that cell's value in the effort 2d array
        if current_effort >= effort[current_m][current_n]:
            # then check each of the next positions/moves which are the equivalent of adjacent vertices
            for i, j in adjacents:
                # check if a valid move based on the valid indexes of the arary
                if 0 <= current_m + i < m and 0 <= current_n + j < n:
                    # find new effort value for that move
                    new_effort = max(current_effort,
                                     abs(puzzle[current_m][current_n] - puzzle[current_m + i][current_n + j]))
                    # if is the less than what exists in that move's next cell
                    if new_effort < effort[current_m + i][current_n + j]:
                        # pop from pq
                        heapq.heappush(pq, (current_m + i, current_n + j, new_effort))
                        # update it in the effort 2d array
                        effort[current_m + i][current_n + j] = new_effort
    # print(f"Final results:\n Effort: {effort}\n PQ: {pq}")
    return effort[m - 1][n - 1]


print(minEffort([[1, 3, 5], [2, 8, 3], [3, 4, 5]]))
print(minEffort([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
