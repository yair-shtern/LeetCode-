# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping
# you from robbing each of them is that adjacent houses have security systems connected and it
# will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dynamicArray = [nums[0], nums[1]]
        for i in range(2, len(nums)):
            curMax = max(dynamicArray[-2], dynamicArray[-1] - nums[i - 1])
            dynamicArray.append(nums[i] + curMax)
        return max(dynamicArray[-1], dynamicArray[-2])
