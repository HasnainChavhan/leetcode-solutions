"""LeetCode #242: Valid Anagram (Easy)"""
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    """Determine if t is an anagram of s.
    Time Complexity: O(N)
    Space Complexity: O(1) - fixed alphabet size 26
    """
    return Counter(s) == Counter(t)

def test_is_anagram():
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False
