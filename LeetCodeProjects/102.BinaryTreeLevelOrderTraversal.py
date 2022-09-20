# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:
#
# Input: root = [1]
# Output: [[1]]
# Example 3:
#
# Input: root = []
# Output: []

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections


class Solution:
    def levelOrder(self, root):
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            q_len = len(queue)
            layer = []
            for _ in range(q_len):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    layer.append(node.val)
            if layer:
                res.append(layer)
        return res


if __name__ == '__main__':
    # Input: root = [3,9,20,null,null,15,7]
    # Output: [[3],[9,20],[15,7]]
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(17)))
    Solution().levelOrder(root)
