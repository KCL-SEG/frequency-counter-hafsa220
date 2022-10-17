"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

list = ['0', 4,4,'4','d','d','e',0,'a','d','4']

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        item = str(item)
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1

    print(frequencies)

    return frequencies

frequencies(list)