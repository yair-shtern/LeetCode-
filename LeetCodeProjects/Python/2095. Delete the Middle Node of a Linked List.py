# You are given the head of a linked list. Delete the middle node,
# and return the head of the modified linked list.
#
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing,
# where ⌊x⌋ denotes the largest integer less than or equal to x.
#
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        n = 0
        tmp = head
        while tmp:
            n += 1
            tmp = tmp.next
        middleIndex = n // 2

        tmp = head
        for _ in range(middleIndex - 1):
            tmp = tmp.next

        tmp.next = tmp.next.next
        return head
