"""LeetCode #20: Valid Parentheses (Easy)"""

def is_valid(s: str) -> bool:
    """Determine if an input string containing '()[]{}' is valid.
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

def test_is_valid():
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
