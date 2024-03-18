# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Can you solve it without sorting?
import collections
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # HEAP
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappushpop(heap, num)

        return heapq.heappop(heap)
