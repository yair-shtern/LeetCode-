# You are given an integer array nums and an integer k. You want to
# find a subsequence of nums of length k that has the largest sum.
#
# Return any such subsequence as an integer array of length k.
#
# A subsequence is an array that can be derived from another array
# by deleting some or no elements without changing the order of the remaining elements.
#
#
#
# Example 1:
#
# Input: nums = [2,1,3,3], k = 2
# Output: [3,3]
# Explanation:
# The subsequence has the largest sum of 3 + 3 = 6.
# Example 2:
#
# Input: nums = [-1,-2,3,4], k = 3
# Output: [-1,3,4]
# Explanation:
# The subsequence has the largest sum of -1 + 3 + 4 = 6.
# Example 3:
#
# Input: nums = [3,4,3,3], k = 2
# Output: [3,4]
# Explanation:
# The subsequence has the largest sum of 3 + 4 = 7.
# Another possible subsequence is [4, 3].

class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = list(enumerate(nums))
        arr.sort(key=lambda x: x[1])
        idx = [i for i, j in arr[-k:]]
        idx.sort()
        return [nums[i] for i in idx]

        # another solution:
        # visited = [False] * len(nums)
        # minimum = min(nums) - 1
        # for i in range(k):
        #     curr_max = minimum
        #     curr_max_ind = -1
        #     for j in range(len(nums)):
        #         if nums[j] > curr_max and not visited[j]:
        #             curr_max_ind = j
        #             curr_max = nums[curr_max_ind]
        #     visited[curr_max_ind] = True
        # res = []
        # for i in range(len(nums)):
        #     if visited[i]:
        #         res.append(nums[i])
        # return res


if __name__ == '__main__':
    print(Solution().maxSubsequence([-1, -2, 3, 4], 3))
