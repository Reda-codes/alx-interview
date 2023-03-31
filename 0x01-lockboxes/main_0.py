#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll
'''
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

boxes = [ [10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], [5, 1, 9, 1], [], [6, 6, 9, 4, 3, 2, 3, 8, 5], [9, 4], [4, 2, 5, 1, 1, 6, 4, 5, 6], [9, 5, 8, 8], [6, 2, 8, 6] ]
print(canUnlockAll(boxes))

boxes = [ [7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], [7, 3], [7, 9, 10, 10, 8, 9, 2, 5], [7, 2, 2, 4, 4, 2, 4, 8, 7], [4, 2, 9, 6, 6, 5, 5], ]
print(canUnlockAll(boxes))

boxes = [[36, 37, 55, 26, 92, 24, 23, 23, 88, 86, 85, 43, 36, 4, 87, 66, 95, 18, 68, 30, 49, 63, 30, 33, 14], [77, 74, 18, 48, 51, 19, 10, 77, 82, 6, 82, 74, 25, 99, 100, 86, 6, 98, 44, 18, 99, 42, 35, 7, 60, 25, 38, 83, 79, 46, 1, 79, 89, 53, 78, 22, 53, 35, 58, 47, 41], [97, 46, 25, 56, 35, 63, 12, 15, 42, 96, 66], [20, 44, 68, 13, 66, 68, 68, 68, 81, 62, 4, 20, 88, 39, 42, 57, 59, 64, 99, 27, 34, 4, 97, 82, 2, 7, 77, 37, 60, 45, 36, 73, 47, 92, 64, 79, 12, 44, 19, 67, 95, 86, 71, 19, 83, 96, 55, 92, 65, 14, 66, 63, 67, 4, 80, 18, 3, 12], [93, 89, 92, 73, 31, 96, 36, 66, 23, 42, 56, 7, 89, 31, 93, 57, 68, 24, 93, 97, 71, 76, 48, 72, 79, 52, 57, 27, 35, 22, 71, 97, 25, 39, 83, 50, 81, 66, 26, 91, 63, 3, 41, 40, 20, 43, 90, 95, 92, 26, 44, 61, 38, 31, 52, 77, 100, 79, 64, 92, 86, 30, 72, 69, 30, 6, 97, 2, 61, 50, 36, 35, 90, 73, 75, 35, 11, 31, 13, 37, 8, 51, 21, 17, 70, 34], [71, 77, 89, 58, 8, 92, 94, 5, 31, 11, 16, 10, 79, 10, 38, 34, 75, 39, 15, 58, 88, 49, 65, 64, 58, 1, 17, 98, 84, 2, 83, 49, 54, 19, 25, 24, 45, 60, 6, 14, 92, 82, 92, 27, 19, 38, 62, 41, 3, 41, 21, 43, 55, 7, 13, 35, 55, 4, 67, 3, 90, 43, 73, 93, 15, 81, 96, 30, 72, 60, 21, 59, 52, 35, 15, 14, 99, 98, 80, 6, 35, 30, 99, 67, 15, 85, 56, 13], [95, 60, 40, 84, 18, 44, 10, 51, 13, 30, 41, 6, 10, 11, 87, 24, 20, 21, 27, 31, 59, 17, 60, 16, 27, 41, 23, 93, 65, 9, 89, 72, 81, 69, 63, 54, 60, 90, 64, 47, 42, 49, 24, 13, 39, 85, 6, 45, 19, 52, 60, 56, 90, 39, 79, 35, 24, 12, 81, 65, 100, 38, 3, 58, 13, 26, 2, 6, 54, 47, 51, 66, 57, 54, 73, 55, 64, 85, 22, 100, 46, 6, 94, 89, 94, 48, 49, 14, 50, 30, 17, 77, 72], [79, 93, 97, 26, 4, 16, 89, 28, 76, 57, 27, 16, 69, 31, 98, 73, 21, 43, 71, 29, 85, 77, 75, 49, 47, 64, 27, 13, 36, 3, 41, 82, 87, 98, 8, 19, 36, 93, 70, 25, 67, 41, 96, 10, 80, 70, 37, 98, 59, 39, 76, 30, 32, 85, 7, 56, 97, 71, 46, 1, 84, 54, 60, 98, 74, 1, 9, 56], [48, 79, 91, 12, 78, 71, 42, 40, 92, 97, 8, 27, 21, 81, 89, 3, 7, 58, 26, 13, 68, 14, 68, 72, 31, 50, 1, 39, 14, 65, 98, 55, 10, 97, 85, 78, 26, 87, 34, 78, 74, 83, 51, 35, 56, 43, 60, 39, 94], [3, 69, 11, 27, 25, 41, 56, 47, 20, 100, 29, 86, 51, 36, 31, 39, 41, 20, 84, 1, 76, 53, 51, 75, 28, 31, 24, 30, 82, 9, 49, 36, 51, 18, 76, 90, 13, 48, 56, 70, 61, 58, 73, 71, 3, 22, 100, 82, 28, 51, 43, 72, 74, 27, 97, 65, 86, 32, 56, 86, 72], [58, 20, 29, 1, 81, 92, 12, 72, 71, 2, 81, 51, 67, 52, 79, 31, 53, 50, 29, 53, 72, 89, 9, 13, 59, 96, 42, 61, 13, 4, 77, 95, 75, 49, 84, 87, 76, 68, 61, 27, 88, 27, 59, 96, 58, 94, 97, 52, 37, 47, 37, 84, 51, 20, 66, 31, 65, 92, 58, 59, 52, 94, 65, 25, 20, 41, 2, 13, 37, 4, 30, 7, 26, 93, 26, 28, 40, 84, 46, 16, 59, 8, 100, 26, 7, 16, 15, 71, 4, 18], [38, 26, 18, 51, 44, 71, 85, 99, 87, 8, 32, 32, 51, 40, 79, 34, 77, 37, 28, 57, 26, 67, 83, 81, 24, 83, 22, 4, 45, 13, 79, 19, 93, 78, 16, 16, 62, 15, 6, 87, 23, 19, 65, 22, 45, 41, 27, 65, 49, 71, 99, 55, 19, 97, 100, 34, 88, 95, 27, 38, 24, 72, 16, 57, 54, 12, 80, 52]]
print(canUnlockAll(boxes))
'''
boxes = []

keys = []
for n in range(1, 1000):
    keys = []
    for m in range(1, 1000):
        keys.append(m)
    boxes.append(keys)

print(canUnlockAll(boxes))
