"""
    File name: shortestPath
    Language: Python 3
    Author: Devavrat Kalam
    Description: Find shortest path from one point to another in the given grid.
"""
from typing import List, Tuple


def getNeighbours(grid: List[List[int]], cord: Tuple[int, int]):
    neigbours = []
    # Grid is not said to be of same length and width
    xlen = len(grid)
    ylen = len(grid[0])

    # Possible directions to move
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for d in directions:
        x = cord[0] + d[0]
        y = cord[1] + d[1]
        if (x >= 0) and (x < xlen) and (y >= 0) and (y < ylen):
            if grid[cord[0] + d[0]][cord[1] + d[1]] == 1:
                neigbours.append((cord[0] + d[0], cord[1] + d[1]))
    return neigbours


def shortestCellPath(grid: List[List[int]], sr: int, sc: int, tr: int, tc: int):
    # To store the distance
    visited = {(sr, sc): 0}
    # Acts as to do list of coordinates yet to be explored
    visit = [(sr, sc)]

    while visit:
        tempcord = visit.pop(0)
        neighbours = getNeighbours(grid, tempcord)
        for i in range(len(neighbours)):
            if neighbours[i] not in visited:
                # If the node is already explored, ignore it
                visited[neighbours[i]] = 1 + visited[tempcord]
                visit.append(neighbours[i])

    # If the node was never reached
    if (tr, tc) not in visited:
        return -1
    return visited[(tr, tc)]


def main():
    # # Test cases:
    grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
    s = (0, 0, 2, 0)

    # grid = [[1, 1, 1, 1], [0, 0,0,1]]
    # sr, sc, tr, tc = 1, 3, 0, 0

    # grid = [[1, 0, 1], [0, 0, 0]]
    # sr, sc, tr, tc = 0, 0, 0, 2

    print(shortestCellPath(grid, *s))


if __name__ == "__main__":
    main()
