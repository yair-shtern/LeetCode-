# Given a root node reference of a BST and a key, delete the node with the given key in the BST.
# Return the root node reference (possibly updated) of the BST.
#
# Basically, the deletion can be divided into two stages:
#
# 1. Search for a node to remove.
# 2. If the node is found, delete the node.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # If the node has both left and right children
            temp = self.findMinNode(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val)

        return root

    def findMinNode(self, root):
        while root.left:
            root = root.left
        return root
