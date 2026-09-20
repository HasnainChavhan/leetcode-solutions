"""LeetCode #226: Invert Binary Tree (Easy)"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Invert a binary tree.
    Time Complexity: O(N)
    Space Complexity: O(H)
    """
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

def test_invert_tree():
    root = TreeNode(4, TreeNode(2), TreeNode(7))
    inverted = invert_tree(root)
    assert inverted.left.val == 7
    assert inverted.right.val == 2
