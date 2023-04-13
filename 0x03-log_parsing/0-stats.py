#!/usr/bin/python3
''' script that reads stdin line by line and computes metrics '''
import sys


count = 0
totalSize = 0
statusList = []

for line in sys.stdin:
    lst = line.split(' ')
    status = int(lst[-2])
    size = int(lst[-1])

    if count == 10:
        print(f'File size:{totalSize}')
        count = 0
        statusList.sort()
        printed = []

        for el in statusList:
            if el not in printed:
                print(f'{el}: {statusList.count(el)}')
                printed.append(el)
        statusList = []

    count += 1
    totalSize += size
    statusList.append(status)
