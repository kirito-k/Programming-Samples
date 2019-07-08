"""
    File name: time_interval.py
    Authod: Devavrat Kalam
    Language: Python 3.x
    Description: Given pairs time intervals (start, end), determine minimum number of classroom required
    Time Complexity: O(n log(n))
"""


def time_interval(intervals: List[Tuple[int, int]]) -> int:
    """
    Find minimum number of rooms need
    :param intervals: list of pairs of start and end times
    :return: minimum rooms required
    """

    start = []
    finish = []
    for elems in intervals:
        start.append(elems[0])
        finish.append(elems[1])

    # Sorting the start and end times separately
    start.sort()
    finish.sort()

    index1, index2 = 0, 0
    current_rooms = 0
    max_rooms = 0
    # The logic below is, we add each room when current finish time is greater than current start time
    # This informs us whether how many times are collapsing with each other at any time
    while (index1 < len(start)) and (index2 < len(finish)):
        if start[index1] < finish[index2]:
            current_rooms += 1
            index1 += 1
        else:
            index2 += 1
            max_rooms = max(max_rooms, current_rooms)
            current_rooms -= 1
    max_rooms = max(max_rooms, current_rooms)
    return max_rooms

def main():
    # Test cases:
    intervals = [
        (30, 75),
        (0, 50),
        (60, 150)
    ]
    # intervals = [(0, 10),(11, 20),(21, 30)]
    # intervals = [(0, 10),(10, 20),(20, 30)]
    # intervals = [(2, 30),(1, 20),(0, 10)]
    # intervals = [(1, 2)]
    # intervals = []

    print(time_interval(intervals))

if __name__ == '__main__':
    main()
