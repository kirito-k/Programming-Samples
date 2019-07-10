"""
    File name: powerful_int.py
    Authod: Devavrat Kalam
    Language: Python 3.x
    Description: Given x, y, bound, find out which of the numbers formed by x^i + y^j which are less than equal to bound
    Time Complexity: O(a * b) where a and b are i max and j max respectively
"""

from typing import List


def powerfulIntegers(x: int, y: int, bound: int) -> List[int]:
    # minimum addition can be 2. If bound is less than
    if bound < 0:
        return []

    # We will calculate the maximum possible values i and j can hold for the condition to stay valid
    max_i = 0
    max_j = 0
    while y ** (max_j + 1) < bound and y != 1:
        max_j += 1
    while x ** (max_i + 1) < bound and x != 1:
        max_i += 1

    # We will use a set for its unique elements nature
    s = set()
    # Assume this setting as a matrix where i is rows and j is the column.
    i = 0
    j = max_j
    while j >= 0 and i <= max_i:
        num = x ** (i) + y ** (j)
        # If the num is valid, add all the elements for this row i from that column to 0th column
        if num <= bound:
            for index in range(j, -1, -1):
                something = x ** (i) + y ** (index)
                s.add(something)
            # Increase the row
            i += 1
        else:
            # Decrease the column since j is causing out of bound case
            j -= 1

    # We need our answer in form of list
    return list(s)


def main():
    # Test cases
    print(powerfulIntegers(2, 3, 10))
    # print(powerfulIntegers(2, 3, 0))
    # print(powerfulIntegers(1, 5, 15))
    # print(powerfulIntegers(1, 1, 20))


if __name__ == '__main__':
    main()
