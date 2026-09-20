"""LeetCode #141: Linked List Cycle (Easy / Floyd's Cycle Finding)"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: Optional[ListNode]) -> bool:
    """Determine if the linked list has a cycle using fast and slow pointers.
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def test_has_cycle():
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2 # cycle
    assert has_cycle(n1) == True
    n4.next = None # remove cycle
    assert has_cycle(n1) == False
