#!/usr/bin/python3
"""
N Queens Module
"""
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen in a given position
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """
    Solve the N Queens problem
    """
    def solve(board, row, N):
        """
        Helper function for solving N Queens using backtracking
        """
        if row == N:
            result.append([[i, board[i]] for i in range(N)])
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve(board, row + 1, N)

    result = []
    solve([0] * N, 0, N)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)

    for solution in solutions:
        print(solution)

