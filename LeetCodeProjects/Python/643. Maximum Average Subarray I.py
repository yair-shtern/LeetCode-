# You are given an integer array nums consisting of n elements, and an integer k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.
import math
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = tmpSum = sum(nums[:k])
        l, r = 0, k
        while r < len(nums):
            tmpSum = tmpSum - nums[l] + nums[r]
            maxSum = tmpSum if tmpSum > maxSum else maxSum
            l, r = l + 1, r + 1
        return maxSum / k
