#!/usr/bin/python3
"""Making a perimeter island finder"""


def island_perimeter(grid) -> int:
    # find the height and with of the grid
    # height will be same as the graph y axis
    height = len(grid)
    # width same as the x axis
    width = len(grid[0])
    no_of_islands = 0
    found_one = 0

    for y in range(height):
        for x in range(width):
            if (grid[y][x] == 1):
                no_of_islands += 1
                # check up
                if (y - 1) >= 1 and grid[y - 1][x] == 1:
                    found_one += 1
                # check down
                if (y + 1) < height and grid[y + 1][x] == 1:
                    found_one += 1
                # check left
                if (x - 1) >= 0 and grid[y][x - 1] == 1:
                    found_one += 1
                # check right
                if (x + 1) < width and grid[y][x + 1] == 1:
                    found_one += 1
    perimeter = no_of_islands * 4
    return (perimeter - found_one)    # found_one what is it?
