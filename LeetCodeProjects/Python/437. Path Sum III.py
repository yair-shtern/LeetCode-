# Given the root of a binary tree and an integer targetSum,
# return the number of paths where the sum of the values along the path equals targetSum.
#
# The path does not need to start or end at the root or a leaf,
# but it must go downwards (i.e., traveling only from parent nodes to child nodes).


# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, currSum):
            if not root:
                return
            currSum += root.val
            self.count += d[currSum - targetSum]
            d[currSum] += 1
            dfs(root.left, currSum)
            dfs(root.right, currSum)
            d[currSum] -= 1

        self.count = 0
        d = collections.defaultdict(int)
        d[0] = 1
        dfs(root, 0)
        return self.count
