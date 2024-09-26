#!/usr/bin/python3
"""Making a perimeter island finder"""


def island_perimeter(grid) -> int:
    """Calculate the perimeter of the island in the given grid"""
    height = len(grid)
    width = len(grid[0])
    perimeter = 0

    for y in range(height):
        for x in range(width):
            if grid[y][x] == 1:
                # Start with 4 for each land cell
                perimeter += 4
                # Check up
                if y > 0 and grid[y - 1][x] == 1:
                    print('hit')
                    print(perimeter)
                    perimeter -= 2
                # Check left
                if x > 0 and grid[y][x - 1] == 1:
                    print('hit')
                    print(perimeter)
                    perimeter -= 2
    return perimeter
