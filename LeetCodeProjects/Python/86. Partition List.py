# Given the head of a linked list and a value x,
# partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftDummy, rightDummy = ListNode(), ListNode()
        left, right = leftDummy, rightDummy
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next

        left.next = rightDummy.next
        right.next = None
        return leftDummy.next
