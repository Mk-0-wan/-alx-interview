#!/usr/bin/python3
"""solving the pascal triangle"""
import sys


def pascal_triangle(n):
    """Returns list of lists that form the pascal_triangle
    """

    lst = []
    if n <= 0:
        return lst

    for row in range(n):
        # make a new list for each index
        lst.append([])
        # initialize it with 1(at the beginning) according to the rule
        lst[row].append(1)
        # next phase calculating the middle values using the previous list
        for col in range(1, row):
            # calculate the value at each position
            # [1,1] <- index 1, [1, ([1] + [1]), ... ] <- index 2
            # lst[row].append([row - 1][col - 1])
            lst[row].append(lst[row - 1][col - 1] + lst[row - 1][col])
        # always add the last one to the end of the list
        if (row != 0):
            # from the above example the list was not complete
            # [1,1] <- index 1, [1, ([1] + [1]), 1] <- index 2(updated)
            # [[1,1], [1,2,1], ... ]
            lst[row].append(1)

    return (lst)
