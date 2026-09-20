"""LeetCode #1: Two Sum (Easy)"""
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
