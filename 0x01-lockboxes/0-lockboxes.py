#!/usr/bin/python3
"""
Lockboxes Challenge
"""
def canUnlockAll(boxes):
    keys = set(boxes[0])
    unlocked = set([0])

    while keys:
        boxToUnlock = keys.pop()
        if boxToUnlock not in unlocked:
            unlocked.add(boxToUnlock)
            keys.update(boxes[boxToUnlock])

    return len(unlocked) == len(boxes)
