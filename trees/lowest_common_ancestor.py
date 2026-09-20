"""LeetCode #236: Lowest Common Ancestor of a Binary Tree (Medium)"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """Find LCA of two given nodes in a binary tree.
    Time Complexity: O(N)
    Space Complexity: O(H)
    """
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right

def test_lca():
    p = TreeNode(5)
    q = TreeNode(1)
    root = TreeNode(3, p, q)
    assert lowest_common_ancestor(root, p, q) == root
