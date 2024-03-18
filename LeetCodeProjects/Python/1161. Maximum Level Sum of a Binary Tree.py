# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
#
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.


# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = collections.deque([root])
        maxSum = root.val
        maxLevel, curLevel = 1, 1

        while queue:
            levelLength = len(queue)
            curLevelSum = 0
            for _ in range(levelLength):
                node = queue.popleft()
                curLevelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if curLevelSum > maxSum:
                maxSum, maxLevel = curLevelSum, curLevel
            curLevel += 1

        return maxLevel
