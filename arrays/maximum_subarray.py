"""LeetCode #53: Maximum Subarray (Easy / Kadane's Algorithm)"""
from typing import List

def max_sub_array(nums: List[int]) -> int:
    """Find the contiguous subarray with the largest sum and return its sum.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

def test_max_sub_array():
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sub_array([1]) == 1
    assert max_sub_array([5, 4, -1, 7, 8]) == 23
