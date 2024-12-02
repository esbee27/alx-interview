#!/usr/bin/python3
"""Islanf perimeter module"""

def island_perimeter(grid):
    """Calculate perimeter of land"""
    row_count = len(grid)
    col_count = len(grid[0])

    perimeter = 0
    for i in row_count:
        for j in col_count:
            if grid[i][j]:
                u = if (not i) or grid[i - 1][j] == 0
                d = (i + 1) >= (row_count) or grid[i + 1][j] == 0
                l = if (not j) or grid[i][j - 1] == 0
                k = (j + 1) >= (col_count) or grid[j + 1][i] == 0
                perimeter += u + d + l + k
    return perimeter
