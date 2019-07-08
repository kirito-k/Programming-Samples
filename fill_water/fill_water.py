"""
    File name: fill_water.py
    Authod: Devavrat Kalam
    Language: Python 3.x
    Description: In given array representing wall hights, determine how much water
                 can be trapped between two walls(not the end of array doesn't indicate its a wall).
    TimeComplexity: O(n)
"""
from typing import List

def capacity(arr: List[int]) -> int:
    n = len(arr)
    left_maxes = [0 for _ in range(n)]
    right_maxes = [0 for _ in range(n)]

    current_left_max = 0
    for i in range(n):
        current_left_max = max(current_left_max, arr[i])
        left_maxes[i] = current_left_max

    current_right_max = 0
    for i in range(n - 1, -1, -1):
        current_right_max = max(current_right_max, arr[i])
        right_maxes[i] = current_right_max

    total = 0
    for i in range(n):
        total += min(left_maxes[i], right_maxes[i]) - arr[i]
    return total


def main():
    arr = [3, 2, 1, 5, 8, 0, 3]
    print(capacity(arr))


if __name__ == '__main__':
    main()
