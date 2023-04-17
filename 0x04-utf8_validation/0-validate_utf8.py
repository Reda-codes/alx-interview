#!/usr/bin/python3
"""
Method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """validUTF8 function"""
    for i in data:
        s = chr(i)
        if len(s) == len(s.encode()):
            continue
        else:
            return False
            break
    return True
