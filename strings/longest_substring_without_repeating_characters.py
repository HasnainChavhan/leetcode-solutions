"""LeetCode #3: Longest Substring Without Repeating Characters (Medium)"""

def length_of_longest_substring(s: str) -> int:
    """Find the length of the longest substring without repeating characters.
    Time Complexity: O(N)
    Space Complexity: O(min(N, M))
    """
    char_map = {}
    left = 0
    max_len = 0
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len

def test_length_of_longest_substring():
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
