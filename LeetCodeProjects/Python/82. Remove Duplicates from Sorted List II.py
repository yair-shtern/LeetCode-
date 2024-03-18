# Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, head
        while fast:
            while fast.next and fast.val == fast.next.val:
                # skip the duplicate nodes
                fast = fast.next

            if slow.next == fast:
                # we didnt skip any node -> the next nodes values are not equal
                slow = slow.next
                fast = fast.next
            else:
                # update the next pointer after skipping some nodes
                slow.next = fast.next
                fast = fast.next

        return dummy.next
