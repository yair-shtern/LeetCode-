# Given a binary tree
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        while head:
            dummy = Node()
            tmp = dummy
            while head:
                if head.left:
                    tmp.next = head.left
                    tmp = tmp.next
                if head.right:
                    tmp.next = head.right
                    tmp = tmp.next
                head = head.next
            head = dummy.next
        return root
