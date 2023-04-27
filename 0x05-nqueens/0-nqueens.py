#!/usr/bin/python3
""" The N queens puzzle """
import sys


def nqueens(N):

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
    
    nqueens(int(sys.argv[1]))
