# You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k.
# You must choose a subsequence of indices from nums1 of length k.
#
# For chosen indices i0, i1, ..., ik - 1, your score is defined as:
#
# The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
# It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
# Return the maximum possible score.
#
# A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.
import collections
import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda p: p[1], reverse=True)

        maxScore = 0
        heap = []
        n1sum = 0

        for n1, n2 in pairs:
            heapq.heappush(heap, n1)
            n1sum += n1

            if len(heap) > k:
                n1sum -= heapq.heappop(heap)

            if len(heap) == k:
                maxScore = max(maxScore, n1sum * n2)

        return maxScore
