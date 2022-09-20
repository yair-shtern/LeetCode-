# Given an array of non-negative integers nums, you are initially positioned
# at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# You can assume that you can always reach the last index.
#
#
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [2,3,0,1,4]
# Output: 2
class Solution(object):
    # Jump Game II - num of jumps, starting from index 0
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        left = right = 0
        while right < len(nums) - 1:
            greatest_index = right
            for i in range(left, right + 1):
                curr_reach = i + nums[i]
                if curr_reach > greatest_index:
                    greatest_index = curr_reach
            left = right + 1
            right = greatest_index
            res += 1
        return res