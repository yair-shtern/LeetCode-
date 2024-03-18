# Given the root of a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.


# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = collections.deque([root])
        res = []

        while queue:
            l = len(queue)
            for i in range(l):
                node = queue.popleft()
                if i == l - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res
