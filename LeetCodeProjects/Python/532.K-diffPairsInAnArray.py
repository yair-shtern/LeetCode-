# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
#
# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
#
# 0 <= i, j < nums.length
# i != j
# nums[i] - nums[j] == k
# Notice that |val| denotes the absolute value of val.
#
#
#
# Example 1:
#
# Input: nums = [3,1,4,1,5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.
# Example 2:
#
# Input: nums = [1,2,3,4,5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
# Example 3:
#
# Input: nums = [1,3,1,5,4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
import collections


class Solution:
    def findPairs(self, nums, k: int) -> int:
        # Run time of O(n):
        #
        res = 0
        count_nums_dict = collections.Counter(nums)
        for key in count_nums_dict:
            if (k > 0 and (k + key) in count_nums_dict) or (k == 0 and count_nums_dict[key] > 1):
                res += 1
        return res

        # Run time of O(nlog(n)):
        #
        # res = 0
        # nums.sort()
        # unique_pairs = set()
        #
        # for i in range(len(nums) - 1):
        #     if nums[i] in unique_pairs:
        #         continue
        #     search_for = k + nums[i]
        #     # Binary search
        #     l, r = i + 1, len(nums) - 1
        #     while l <= r:
        #         m = (l + r) // 2
        #         if nums[m] > search_for:
        #             r = m - 1
        #         elif nums[m] < search_for:
        #             l = m + 1
        #         else:  # nums[m] == search_for
        #             unique_pairs.add(nums[i])
        #             res += 1
        #             break
        #
        # return res


if __name__ == '__main__':
    print(Solution().findPairs([1, 2, 4, 4, 3, 3, 0, 9, 2, 3], 3) == 2)
    print(Solution().findPairs([1, 3, 1, 5, 4], 0) == 1)
    print(Solution().findPairs([1, 2, 3, 4, 5], 1) == 4)
    print(Solution().findPairs([3, 1, 4, 1, 5], 2) == 2)
