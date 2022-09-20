# You are given an integer array nums.
# You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
#
#
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what.
# Its maximum jump length is 0, which makes it impossible to reach the last index.
class Solution(object):
    # Jump Game - can we reach the last index starting from index 0?
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums) - 1
        # Go backwards throw the array if we can reach the goal from the
        # i index change the goal to be i
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        # At the end if goal is zero it is mean that from index zero we can reach the last index
        return True if goal == 0 else False
