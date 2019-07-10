"""
    File name: two_cities.py
    Authod: Devavrat Kalam
    Language: Python 3.x
    Description: Given 2D array, where outer loop represents ith person and
                in inner arrays 0th and 1st indices are costs to reach city A and city B respectively,
                Find the minimum cost where A and B city people are in same number
    Time Complexity: O()
"""

from typing import List


def twoCitySchedCost(costs: List[List[int]]) -> int:
    # Sort the list on the difference between A's and B's costs.
    costs.sort(key=lambda x: x[0] - x[1])
    half = len(costs) // 2
    answer = 0
    # Logic - All the first half costs will be minimum on x[0] and rest of they on x[1]
    for index in range(len(costs)):
        answer += costs[index][0] if index < half else costs[index][1]
    return answer


def main():
    # Test cases:
    arr = [[10, 20], [30, 200], [400, 50], [30, 20]]
    # arr = []
    # arr = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    print(twoCitySchedCost(arr))
    pass


if __name__ == '__main__':
    main()
