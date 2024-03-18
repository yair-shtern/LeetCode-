# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        listLen = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            listLen += 1

        leftPrev, cur = dummy, head
        prev = leftPrev
        for _ in range(listLen // k):
            for _ in range(k):
                tmpNext = cur.next
                cur.next = prev
                prev, cur = cur, tmpNext
            leftPrev.next.next = cur
            tmpLP = leftPrev.next
            leftPrev.next = prev
            leftPrev = tmpLP

        return dummy.next
