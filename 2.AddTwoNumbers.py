# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
#
#
# Example 1:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        remainder = 0
        k = 10
        res_head = res_l = None
        while l1 and l2:
            res_val = (l1.val + l2.val + remainder) % k
            node = ListNode(val=res_val)
            if not res_l:
                res_l = res_head = node
            else:
                res_l.next = node
                res_l = res_l.next
            remainder = (l1.val + l2.val + remainder) // k
            l1, l2 = l1.next, l2.next

        while l1:
            res_val = (l1.val + remainder) % k
            node = ListNode(val=res_val)
            if not res_l:
                res_l = res_head = node
            else:
                res_l.next = node
                res_l = res_l.next
            remainder = (l1.val + remainder) // k
            l1 = l1.next

        while l2:
            res_val = (l2.val + remainder) % k
            node = ListNode(val=res_val)
            if not res_l:
                res_l = res_head = node
            else:
                res_l.next = node
                res_l = res_l.next
            remainder = (l2.val + remainder) // k
            l2 = l2.next

        if remainder != 0:
            res_l.next = ListNode(val=remainder, next=None)

        return res_head


if __name__ == '__main__':
    l1 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=None)))
    l2 = ListNode(val=1, next=None)
    Solution().addTwoNumbers(l1, l2)
