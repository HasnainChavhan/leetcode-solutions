"""LeetCode #70: Climbing Stairs (Easy)"""

def climb_stairs(n: int) -> int:
    """Count number of distinct ways to climb n stairs taking 1 or 2 steps.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if n <= 2:
        return n
    one, two = 1, 2
    for _ in range(3, n + 1):
        one, two = two, one + two
    return two

def test_climb_stairs():
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8
