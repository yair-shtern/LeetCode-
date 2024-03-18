# Given a binary array nums, you should delete one element from it.
#
# Return the size of the longest non-empty subarray containing only 1's in the resulting array.
# Return 0 if there is no such subarray.
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result, numZeros, left = 0, 0, 0
        for right in range(len(nums)):
            numZeros += 1 - nums[right]
            while numZeros > 1:
                numZeros -= 1 - nums[left]
                left += 1
            result = max(result, right - left)
        return result
