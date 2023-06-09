#!/usr/bin/python3
'''
function that returns a list of lists of integers
representing the Pascal’s triangle of n
'''


def combi(n1, n2):
    '''function similar to math.comb()'''
    num1 = 1
    num2 = 1
    for i in range(1, n2+1):
        num1 *= (n1 - i + 1)
        num2 *= i
    return num1 // num2


def pascal_triangle(n):
    ''' pascal_triangle(n) function '''
    if n <= 0:
        return []
    else:
        ls = []
        for i in range(n):
            nums = []
            for j in range(0, i+1):
                nums.append(combi(i, j))
            ls.append(nums)
        return ls
