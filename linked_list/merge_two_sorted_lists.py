"""LeetCode #21: Merge Two Sorted Lists (Easy)"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Merge two sorted linked lists and return it as a new sorted list.
    Time Complexity: O(N + M)
    Space Complexity: O(1)
    """
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next

def test_merge_two_lists():
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    merged = merge_two_lists(l1, l2)
    res = []
    while merged:
        res.append(merged.val)
        merged = merged.next
    assert res == [1, 1, 2, 3, 4, 4]
