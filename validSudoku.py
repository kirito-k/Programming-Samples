"""
    File name: validSudoku.py
    Authod: Devavrat Kalam
    Language: Python 3.x
    Description: Determine if a 9x9 Sudoku board is valid.
    Time Complexity: O(n ^ 2)
    LeetCode: #36 Medium
"""

from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    for i in range(9):
        count_row = 0
        count_col = 0
        s_row = set()
        s_col = set()
        for j in range(9):
            if board[i][j].isdigit():
                count_row += 1
                s_row.add(board[i][j])
            if board[j][i].isdigit():
                count_col += 1
                s_col.add(board[j][i])
        if len(s_row) != count_row or len(s_col) != count_col:
            return False

    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            if not gridCheck(board, i, j):
                return False

    return True


def gridCheck(board: List[List[str]], row: int, col: int) -> bool:
    count = 0
    s = set()
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if board[i][j].isdigit():
                count += 1
                s.add(board[i][j])

    if count != len(s):
        return False
    return True


def main():
    # Test cases:
    board = \
        [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]
         ]
    # board = \
    # [[".", ".", ".", "9", ".", ".", ".", ".", "."],
    #  [".", ".", ".", ".", ".", ".", ".", ".", "."],
    #  [".", ".", "3", ".", ".", ".", ".", ".", "1"],
    #  [".", ".", ".", ".", ".", ".", ".", ".", "."],
    #  ["1", ".", ".", ".", ".", ".", "3", ".", "."],
    #  [".", ".", ".", ".", "2", ".", "6", ".", "."],
    #  [".", "9", ".", ".", ".", ".", ".", "7", "."],
    #  [".", ".", ".", ".", ".", ".", ".", ".", "."],
    #  ["8", ".", ".", "8", ".", ".", ".", ".", "."]]
    print(isValidSudoku(board))


if __name__ == '__main__':
    main()
