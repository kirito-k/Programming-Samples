"""
    File name: search_2D_2.py
    Authod: Devavrat Kalam
    Language: Python 3.x
    Description: Search a number in 2D matrix.
    Rules -
         Every numbers is greater than its above and left side numbers
     Time Complexity: O(m + n)
"""
from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    """
    Determine if the matrix has the target value or not
    :param matrix: m x n 2D matrix
    :param target: integer value
    :return:
    """

    # Edge cases
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    """
    Logic -
            We will go from bottom left to right.
            If the current value is greater than the target, that means we can ignore the rest of row
            and move on reducing row count.
            Else increase the column count
    """
    row = len(matrix) - 1
    col = 0
    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            row -= 1
        else:
            col += 1

    return False


def main():
    # Test cases
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    # matrix = []
    # matrix = [
    #           [1,4,7,11,15],
    #           [2,5,8,12,19],
    #           [3,6,9,16,22],
    #           [10,13,14,17,24],
    #           [18,21,23,26,30]
    #           ]
    target = 20

    print(searchMatrix(matrix, target))


if __name__ == '__main__':
    main()
