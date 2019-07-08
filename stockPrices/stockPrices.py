"""
    File name: stockPrice
    Language: Python3
    Author: Devavrat Kalam
    Description: Calculate the maximum profit from stock prices data
"""
from typing import List


def get_max_profit(stock: List[int]) -> int:
    # If there are no two stock prices, we cannot buy and sell
    if len(stock) < 2:
        raise ValueError("Not enough data to calculate profit.")

    # We have to buy first to sell it. Thus, first value is minval
    minval = stock[0]
    # Initial profit
    profit = stock[1] - minval

    for index in range(1, len(stock)):
        currprice = stock[index]

        # Calculate profit
        profit = max(profit, currprice - minval)

        # If there is new minimum value found
        minval = min(minval, currprice)

    return profit


if __name__ == '__main__':
    # Test cases:
    a = [10, 7, 5, 8, 11, 9]
    # a = [0,0,0]
    # a = [1,2,3,4,5]
    # a = [5,4,3,2,1]
    # a = [5]
    print(get_max_profit(a))
