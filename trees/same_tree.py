"""LeetCode #100: Same Tree (Easy)"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """Check if two binary trees are identical in structure and values.
    Time Complexity: O(N)
    Space Complexity: O(H)
    """
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

def test_is_same_tree():
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    t2 = TreeNode(1, TreeNode(2), TreeNode(3))
    t3 = TreeNode(1, TreeNode(2), None)
    assert is_same_tree(t1, t2) == True
    assert is_same_tree(t1, t3) == False
