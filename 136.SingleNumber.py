# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.
#
#
#
# Example 1:
#
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
#
# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:
#
# Input: nums = [1]
# Output: 1

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set()
        for item in nums:
            if item in nums_set:
                nums_set.remove(item)
            else:
                nums_set.add(item)
        return nums_set.pop()

        # Another solution:
        # nums.sort()
        # left = 0
        # right = len(nums) - 1
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid - 1] == nums[mid]:
        #         if (right - mid) % 2 == 0:
        #             right = mid - 2
        #         else:
        #             left = mid + 1
        #     elif nums[mid + 1] == nums[mid]:
        #         if (right - mid) % 2 == 0:
        #             left = mid + 2
        #         else:
        #             right = mid - 1
        #     else:
        #         return nums[mid]
        # return nums[left]
