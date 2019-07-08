"""
    File name: MinimumInt.py
    Language: Python 3
    Author name: Devavrat Kalam
    Description: Find smallest positive number(Greater than 1) which is not present in list.
"""
from typing import List

def minimumInt(A: List[int]) -> int:
    # start of array
    x = 1

    # dictionary which stored seen integers. It is used for fast lookup
    seen = {
    half_size = len(A) // 2
    max_len = len(A)

    for i in range(half_size):
        # Check array from front
        if A[i] not in seen:
            seen[A[i]] = True

        # Check array from back
        if A[-(i + 1)] not in seen:
            seen[A[-(i + 1)]] = True

    # Assigning relevant value to x
    while True:
        if x in seen:
            x += 1
        else:
            break

    # If array was of odd length, we will miss out middle value.
    # This handles middle value
    if max_len % 2 != 0:
        if A[half_size] not in seen:
            seen[A[half_size]] = True

    return x


if __name__ == '__main__':
    print(minimumInt([ 1, 1, 1, 1, 1]))
    print(minimumInt([ -99, 99, -10, 10, -1, 1]))
    print(minimumInt([ 1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10]))
