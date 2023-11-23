"""
Example
Input: puzzle[][] = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
Output: 1
Explanation: The minimal effort route would be [1, 2, 3, 4, 5] which has an effort of value 1.
This is better than other routes for instance, route [1, 3, 5, 3, 5] which has an effort of 2.
"""

import heapq


def minEffort(puzzle):
    m = len(puzzle)
    n = len(puzzle[0])
    adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    effort = [[1000] * n for j in range(m)]
    effort[0][0] = 0
    pq = [(0, 0, 0)]
    while len(pq) > 0:
        # print(effort)
        # print(pq)
        current_m, current_n, current_effort = heapq.heappop(pq)
        if current_effort >= effort[current_m][current_n]:
            for i, j in adjacents:
                if 0 <= current_m + i < m and 0 <= current_n + j < n:
                    new_effort = max(current_effort,
                                     abs(puzzle[current_m][current_n] - puzzle[current_m + i][current_n + j]))
                    if new_effort < effort[current_m + i][current_n + j]:
                        heapq.heappush(pq, (current_m + i, current_n + j, new_effort))
                        effort[current_m + i][current_n + j] = new_effort
    # print(f"Final results:\n Effort: {effort}\n PQ: {pq}")
    return effort[m - 1][n - 1]


print(minEffort([[1, 3, 5], [2, 8, 3], [3, 4, 5]]))
print(minEffort([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
