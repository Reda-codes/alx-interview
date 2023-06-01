#!/usr/bin/python3
def isWinner(x, nums):
    """ Is Winner function """
    mariaWins = 0
    benWins = 0

    if mariaWins > benWins:
        return "Maria"
    elif benWins > mariaWins:
        return "Ben"
    else:
        return None
