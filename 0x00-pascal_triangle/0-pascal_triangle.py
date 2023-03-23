#!/usr/bin/python3
'''
function that returns a list of lists of integers
representing the Pascal’s triangle of n
'''


def pascal_triangle(n):
    ''' pascal_triangle(n) function '''
    if n <= 0:
        return []
    else:
        ls = []
        for i in range(n):
            nums = []
            for j in range(i+1):
                nums.append(math.comb(int(i), int(j)))
            ls.append(nums)
        return ls
