"""LeetCode #125: Valid Palindrome (Easy)"""

def is_palindrome(s: str) -> bool:
    """Determine if a string is a palindrome considering only alphanumeric characters and ignoring cases.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome(" ") == True
