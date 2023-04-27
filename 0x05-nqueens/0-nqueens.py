#!/usr/bin/python3
""" The N queens puzzle """
import sys


def nqueens(N):

    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def queenLoc(board, row, col):
        for r, c in board:
            if r == row or c == col or r+c == row+col or r-c == row-col:
                return False
        return True

    def solve(board, row):
        if row == N:
            print(board)
            return None

        for col in range(N):
            if queenLoc(board, row, col):
                solve(board + [[row, col]], row+1)

    solve([], 0)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
