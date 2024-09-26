#!/usr/bin/python3
"""My own way of making it"""


def sop(grid):
    """takes in a grid which is just a list of list integers"""
    # find the length of the column
    col_len = len(grid)
    # find the length of the row
    row_len = len(grid[0])
    n_island = 0
    match  = 0

    for i in range(col_len):
        for j in range(row_len):
            if (grid[i][j] == 1):
                n_island += 1
                print(grid[i][j], end=', ' if j < row_len else '.')
                if (i - 1) >= 1 and grid[i - 1][j] == 1:
                    match += 1
                if (i + 1) < col_len and grid[i + 1][j] == 1:
                    match += 1
                if (j - 1) >= 0 and grid[i][j - 1] == 1:
                    match += 1
                if (j + 1) < row_len and grid[i][j + 1] == 1:
                    match += 1
        print()

    print(n_island)
    print(n_island * 4)
    print(match)
    print((n_island * 4) - match)

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    sop(grid)

