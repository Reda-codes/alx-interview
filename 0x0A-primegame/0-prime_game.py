#!/usr/bin/python3
def isWinner(x, nums):
    """ Is Winner function """
    mariaWins = 0
    benWins = 0
    
    def isPrime(num):
        """ Check  if number is prime """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(x):
        n = nums[i]
        primeCount = 0
        for j in range(1, n+1):
            if isPrime(j):
                primeCount += 1
        
        if primeCount % 2 == 0:
            benWins += 1
        else:
            mariaWins += 1


    if mariaWins > benWins:
        return "Maria"
    elif benWins > mariaWins:
        return "Ben"
    else:
        return None
