"""LeetCode #11: Container With Most Water (Medium)"""
from typing import List

def max_area(height: List[int]) -> int:
    """Find two lines that together with the x-axis form a container containing the most water.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    left, right = 0, len(height) - 1
    max_w = 0
    while left < right:
        h = min(height[left], height[right])
        max_w = max(max_w, h * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_w

def test_max_area():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
