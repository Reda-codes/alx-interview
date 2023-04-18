#!/usr/bin/python3
"""
Method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """validUTF8 function"""
    try:
        byteData = bytes(data)
        byteData.decode('utf-8')
    except UnicodeDecodeError:
        return False
    except ValueError:
        return False
    return True
    
