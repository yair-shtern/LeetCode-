# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroInd = 0
        for ind in range(len(nums)):
            if nums[zeroInd] == 0 and nums[ind] != 0:
                nums[zeroInd], nums[ind] = nums[ind], 0
            if nums[zeroInd] != 0:
                zeroInd += 1
