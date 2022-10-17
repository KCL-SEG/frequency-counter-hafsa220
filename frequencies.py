"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

list = [1,2,3,4]

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1

    print(frequencies)

    return frequencies

frequencies(list)