"""LeetCode #5: Longest Palindromic Substring (Medium)"""

def longest_palindrome(s: str) -> str:
    """Find the longest palindromic substring in s.
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    if not s:
        return ""
    
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    res = ""
    for i in range(len(s)):
        p1 = expand(i, i)
        p2 = expand(i, i + 1)
        res = max(res, p1, p2, key=len)
    return res

def test_longest_palindrome():
    assert longest_palindrome("babad") in ["bab", "aba"]
    assert longest_palindrome("cbbd") == "bb"
