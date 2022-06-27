#!/usr/bin/python3
"""Solves the N queens problem"""
from sys import argv
N = 0
board = []


def argchecks():
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        global N
        N = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if int(argv[1]) < 4:
        print("N must be at least 4")
        exit(1)


def print_solution():
    solution = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def is_safe(row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i -= 1
            j -= 1
    i = row
    j = col
    while j >= 0 and i < N:
        if board[i][j]:
            return False
        i += 1
        j -= 1
    return True


def nqueens(col):
    """Calculates nqueen solution"""
    global board
    if col == N:
        print_solution()
        return True
    retval = False
    for i in range(N):
        if is_safe(i, col):
            board[i][col] = 1
            retval = nqueens(col + 1) or retval
            board[i][col] = 0
    return retval


def nqueens_driver():
    """Drives program"""
    global board
    argchecks()
    board = [[0] * N for _ in range(N)]
    nqueens(0)

nqueens_driver()
