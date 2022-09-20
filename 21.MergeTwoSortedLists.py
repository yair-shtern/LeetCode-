# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#
# Example 1:
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        curr_node_l1, curr_node_l2 = list1, list2
        new_list, head = None, None
        while curr_node_l1 and curr_node_l2:
            minimum = min(curr_node_l1.val, curr_node_l2.val)
            node = ListNode(val=minimum, next=None)
            if not new_list:
                new_list = head = node
            else:
                new_list.next = node
                new_list = new_list.next

            if minimum == curr_node_l1.val:
                curr_node_l1 = curr_node_l1.next
            else:
                curr_node_l2 = curr_node_l2.next

        while curr_node_l1:
            new_list.next = ListNode(val=curr_node_l1.val, next=None)
            new_list = new_list.next
            curr_node_l1 = curr_node_l1.next

        while curr_node_l2:
            new_list.next = ListNode(val=curr_node_l2.val, next=None)
            new_list = new_list.next
            curr_node_l2 = curr_node_l2.next

        return head


if __name__ == '__main__':
    # Input: list1 = [1,2,4], list2 = [1,3,4]
    # Output: [1,1,2,3,4,4]
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    Solution().mergeTwoLists(l1, l2)
