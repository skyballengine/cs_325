import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(parent_dir)
sys.path.append(parent_dir)
from showcallstack import showcallstack


def puzzle(n):
    memo = {}
    return puzzle_helper(n, memo)


def puzzle_helper(n, memo):
    showcallstack()
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    if n in memo:
        return memo[n]
    max_val = 0
    for i in range(1, n + 1):
        max_val = max(max_val, puzzle_helper(n - 1, memo) + puzzle_helper(n - 2, memo))
    memo[n] = max_val
    return memo[n]


print(puzzle(2))
print(puzzle(3))
print(puzzle(4))

