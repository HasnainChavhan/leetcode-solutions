"""LeetCode #300: Longest Increasing Subsequence (Medium)"""
from typing import List
import bisect

def length_of_lis(nums: List[int]) -> int:
    """Find length of longest strictly increasing subsequence using binary search.
    Time Complexity: O(N log N)
    Space Complexity: O(N)
    """
    tails = []
    for num in nums:
        idx = bisect.bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return len(tails)

def test_length_of_lis():
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([7, 7, 7, 7, 7]) == 1
