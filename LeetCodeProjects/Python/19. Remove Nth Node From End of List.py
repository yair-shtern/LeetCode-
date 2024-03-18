# Given the head of a linked list, remove the nth node from the end of the list and return its head.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head

        # Move right pointer n nodes ahead
        for _ in range(n):
            right = right.next

        # Move both pointers until right reaches the end
        while right:
            left, right = left.next, right.next

        # Remove the nth node from the end
        left.next = left.next.next

        return dummy.next
