# Given an array of non-negative integers arr, you are initially
# positioned at start index of the array. When you are at index i,
# you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
#
# Notice that you can not jump outside of the array at any time.
#
#
#
# Example 1:
#
# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation:
# All possible ways to reach at index 3 with value 0 are:
# index 5 -> index 4 -> index 1 -> index 3
# index 5 -> index 6 -> index 4 -> index 1 -> index 3
# Example 2:
#
# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true
# Explanation:
# One possible way to reach at index 3 with value 0 is:
# index 0 -> index 4 -> index 1 -> index 3
# Example 3:
#
# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.
class Solution(object):
    # Jump Game III - starting from a given index and can go ether whey
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        visited = [False] * len(arr)
        from collections import deque
        indexes_queue = deque()
        indexes_queue.append(start)

        while indexes_queue:
            i = indexes_queue.popleft()
            if arr[i] == 0:
                return True

            if visited[i]:
                continue

            left = i - arr[i]
            right = i + arr[i]
            if left >= 0:
                indexes_queue.append(left)
            if right < len(arr):
                indexes_queue.append(right)
            visited[i] = True
        return False