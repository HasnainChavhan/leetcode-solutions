"""LeetCode #206: Reverse Linked List (Easy)"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """Reverse a singly linked list iteratively.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def test_reverse_list():
    head = ListNode(1, ListNode(2, ListNode(3)))
    rev = reverse_list(head)
    assert rev.val == 3
    assert rev.next.val == 2
    assert rev.next.next.val == 1
