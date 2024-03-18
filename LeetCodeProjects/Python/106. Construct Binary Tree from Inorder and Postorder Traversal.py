# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the
# postorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIndx = {v: i for i, v in enumerate(inorder)}
        root = None

        def helper(l: int, r: int):
            if l > r:
                return None
            root = TreeNode(postorder.pop())
            ind = inorderIndx[root.val]
            root.left = helper(l, ind - 1)
            root.right = helper(ind + 1, r)

        helper(0, len(postorder) - 1)
        return root
