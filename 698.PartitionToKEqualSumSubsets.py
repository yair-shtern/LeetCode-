# Given an integer array nums and an integer k, return true if it is possible
# to divide this array into k non-empty subsets whose sums are all equal.
#
#
#
# Example 1:
#
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# Example 2:
#
# Input: nums = [1,2,3,4], k = 3
# Output: false

class Solution(object):
    # Partition to K Equal Sum Subsets
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) % k:
            return False
        nums.sort(reverse=True)
        target = sum(nums) / k
        used = [False] * len(nums)

        def backtrack(start_index, partitions, subset_sum):
            if partitions == 0:
                return True
            if subset_sum == target:
                return backtrack(0, partitions - 1, 0)
            for j in range(start_index, len(nums)):
                if used[j] or subset_sum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j + 1, partitions, subset_sum + nums[j]):
                    return True
                used[j] = False
            return False

        return backtrack(0, k, 0)
