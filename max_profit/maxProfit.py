"""
    File name: maxProfit.py
    Authod: Devavrat Kalam
    Language: Python 3.x
    Description: Compute maximum profit from a single valid transaction(buy first and sell later) from given array
    Time Complexity: O(n)
"""
from typing import List

def maxProfit(arr: List[int]) -> int:
    """
    Compute the maximum profit
    :param arr: arr of integers
    :return: Maximum profit
    """

    if not arr:
        return 0

    # Initializing min and max vals to extreme
    minVal = max(arr)
    maxVal = 0

    for elem in arr:
        if elem < minVal:
            # if current value is less than current minimumVal, replace it
            minVal = elem
        elif (elem - minVal) > maxVal:
            # If profit is more than current profit, replace it
            maxVal = elem - minVal

    return maxVal


def main():
    # Test cases:
    time_intervals = [7, 2, 5, 4, 3, 10]
    # time_intervals = [1, 1, 1]
    # time_intervals = [7, 6, 5, 4, 3, 2, 1]
    # time_intervals = [7, 8, 9, 10]
    # time_intervals = [10]
    # time_intervals = []

    print(maxProfit(time_intervals))


if __name__ == '__main__':
    main()

