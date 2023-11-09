from random import random, randint, randrange
import numpy as np


# Build 2d matrix and add parameters
def n_queens(n):
    board = [[0 for m in range(n)] for n in range(n)]
    solve_n_queens(board, 0, n, n)
    return board


def solve_n_queens(board, row, N, remaining):
    # base case
    if remaining == 0:
        return True

    for col in range(1, N):
        if is_attacked(row, col, board, N):
            continue
        else:
            board[row][col] = 1
            if solve_n_queens(board, row + 1, N, remaining - 1):
                return True
            else:
                board[row][col] = 0
                solve_n_queens(board, row - 1, N, remaining + 1)
    return False


def is_attacked(row, col, board, N):
    if board[row-1][col-1] == 1:
        for i in range(1, row):
            if board[row - i][col] == 1:
                return True
            elif board[row - i][col - i] == 1:
                return True
            elif board[row - i][col + i] == 1:
                return True
    else:
        return False

def create_random_2darr():
    arr_1 = [[0 for x in range(4)] for y in range(4)]
    arr_2 = [[0 for x in range(8)] for y in range(8)]
    for i in range(4):
        x = randint(0, 3)
        # print(x)
        arr_1[i][x] = 1
    for i in range(8):
        x = randint(0, 7)
        # print(x)
        arr_2[i][x] = 1
    for j in range(len(arr_1)):
        print(arr_1[j])
    for j in range(len(arr_2)):
        print(arr_2[j])
    return arr_1, arr_2

def test_attacked(ds):
    N = len(ds)
    print(N)
    for i in range(1, N + 1):
        print(f"Row {i}")
        for j in range(1, N + 1):
            print(f"Row {i} Col {j}")
            if is_attacked(i, j, ds, N):
                print(f"Row {i} Col {j} is attacked")


# arr_1 = np.zeros(4)

arr_1, arr_2 = create_random_2darr()
print(type(arr_1))
print(type(arr_2))
test_attacked(arr_1)
test_attacked(arr_2)
