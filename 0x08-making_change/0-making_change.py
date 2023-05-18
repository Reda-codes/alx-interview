#!/usr/bin/python3
''' makeChange file '''


def makeChange(coins, total):
    ''' makeChange function '''
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coinsCount = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            coinsCount += 1
    if total == 0:
        return coinsCount
    else:
        return -1
