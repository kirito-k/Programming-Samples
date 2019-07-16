"""
    File name: max_water.py
    Authod: Devavrat Kalam
    Language: Python 3.x
    Description: Given n non-negative integers representing walls, find most water that can be contained
    Time Complexity: O(n ^ 2)
    LeetCode: #11 Medium
"""

from typing import List


def maxArea(height: List[int]) -> int:
    i = 0
    j = len(height) - 1
    answer = 0
    while i != j:
        if height[i] < height[j]:
            answer = max(answer, (j - i) * min(height[j], height[i]))
            i += 1
        else:
            answer = max(answer, (j - i) * min(height[j], height[i]))
            j -= 1
    return answer


def main():
    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # arr = [8, 2, 4, 6, 2, 7]
    # arr = [0,0,0]
    # arr = [1,1]
    print(maxArea(arr))


if __name__ == '__main__':
    main()
