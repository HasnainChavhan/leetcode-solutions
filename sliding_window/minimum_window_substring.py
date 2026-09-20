"""LeetCode #76: Minimum Window Substring (Hard)"""
from collections import Counter

def min_window(s: str, t: str) -> str:
    """Find the minimum window substring of s such that every character in t is included in the window.
    Time Complexity: O(N)
    Space Complexity: O(K)
    """
    if not s or not t:
        return ""
    target_counts = Counter(t)
    required = len(target_counts)
    filtered_s = []
    for i, char in enumerate(s):
        if char in target_counts:
            filtered_s.append((i, char))
    
    left = right = 0
    formed = 0
    window_counts = {}
    ans = (float("inf"), None, None)
    
    while right < len(filtered_s):
        char = filtered_s[right][1]
        window_counts[char] = window_counts.get(char, 0) + 1
        if window_counts[char] == target_counts[char]:
            formed += 1
        while left <= right and formed == required:
            char = filtered_s[left][1]
            end = filtered_s[right][0]
            start = filtered_s[left][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)
            window_counts[char] -= 1
            if window_counts[char] < target_counts[char]:
                formed -= 1
            left += 1
        right += 1
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

def test_min_window():
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
