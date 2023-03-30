#!/usr/bin/python3
"""
Lockboxes Challenge
"""


def canUnlockAll(boxes):
    keys = [0]
    unlocked = set()

    while keys:
        box = keys.pop()
        unlocked.add(box)
        for key in boxes[box]:
            if key not in unlocked:
                keys.append(key)

    for i in range(len(boxes)):
        if i not in unlocked:
            return False
    return True