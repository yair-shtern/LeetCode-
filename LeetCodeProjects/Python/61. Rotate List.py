# Given the head of a linked list, rotate the list to the right by k places.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        headInd = length - k
        prev, cur = None, head
        for _ in range(headInd):
            prev, cur = cur, cur.next

        prev.next = None
        tail.next = head

        return cur

        # def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #     dummy = ListNode(0, head)
        #
        #     nodesStack = []
        #     while head:
        #         nodesStack.append(head)
        #         head = head.next
        #
        #     k = k % len(nodesStack) if len(nodesStack) != 0 else 0
        #     tmp = dummy
        #     for i in range(len(nodesStack) - k, len(nodesStack)):
        #         nodesStack[i].next = None
        #         print(nodesStack[i].val)
        #         tmp.next = nodesStack[i]
        #         tmp = tmp.next
        #
        #     for i in range(len(nodesStack) - k):
        #         nodesStack[i].next = None
        #         print(nodesStack[i].val)
        #         tmp.next = nodesStack[i]
        #         tmp = tmp.next
        #
        #     return dummy.next
