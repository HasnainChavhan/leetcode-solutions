"""LeetCode #121: Best Time to Buy and Sell Stock (Easy)"""
from typing import List

def max_profit(prices: List[int]) -> int:
    """Find the maximum profit you can achieve from a single transaction.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    min_price = float('inf')
    max_p = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_p:
            max_p = price - min_price
    return max_p

def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
