"""LeetCode #104: Maximum Depth of Binary Tree (Easy)"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: Optional[TreeNode]) -> int:
    """Find maximum depth of a binary tree.
    Time Complexity: O(N)
    Space Complexity: O(H) recursion stack
    """
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def test_max_depth():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3
