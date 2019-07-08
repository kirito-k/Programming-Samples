"""
    File name: sortedHasSum.py
    Language: Python3
    Author name: Devavrat Kalam
    Description: In given sorted array, find if a pair exists whose sum is equal to given number x, in O(n).
                 No hash data structures allowed.
"""
from typing import List


def sortedHasSum(s: List[int], x: int) -> bool:
    low = 0
    high = len(s)-1

    while True:
        # If no sum-pair exists
        if low > high:
            return False

        # sum of low and high numbers
        tempSum = s[low] + s[high]
        if tempSum == x:
            return True
        elif tempSum > x:
            # If sum is more than x, it means our highest number is too high.
            # So we reduce it
            high -= 1
        else:
            # If sum is less than x, it means our lowest number is too low.
            # So we increase it
            low += 1


if __name__ == '__main__':

    # Test cases:
    print(sortedHasSum([ 1, 2, 3, 7, 8, 14, 18, 30], 20))
    print(sortedHasSum([ -20, -7, -3, -1, 0, 15, 30, 100], -5))
