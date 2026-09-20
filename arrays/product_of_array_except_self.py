"""LeetCode #238: Product of Array Except Self (Medium)"""
from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    """Return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
    Time Complexity: O(N)
    Space Complexity: O(1) auxiliary
    """
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

def test_product_except_self():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
