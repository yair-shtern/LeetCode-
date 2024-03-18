# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder
# is the inorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = {v: i for i, v in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return None
            root = TreeNode(preorder.pop(0))
            m = inorderIdx[root.val]
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root

        return helper(0, len(inorder) - 1)
