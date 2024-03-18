# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that
# i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
import math
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a, b = math.inf, math.inf
        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else: 
                return True
        return False
