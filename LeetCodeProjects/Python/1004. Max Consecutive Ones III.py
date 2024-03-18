# Given a binary array nums and an integer k,
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxOnes = numOnes = l = 0
        for r in range(len(nums)):
            numOnes += nums[r]
            if r - l + 1 - numOnes > k:
                numOnes -= nums[l]
                l += 1

            maxOnes = max(maxOnes, numOnes + r - l + 1)
        return maxOnes
