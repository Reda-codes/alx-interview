#!/usr/bin/python3
"""
Lockboxes Challenge
"""


def canUnlockAll(boxes):
    keys = [0]
    unlocked = set()
    visited = []

    while keys:
        box = keys.pop()
        unlocked.add(box)
        visited.append(box)

        for key in boxes[box]:
            if key not in visited and key < len(boxes):
                keys.append(key)

    return len(unlocked) == len(boxes)
