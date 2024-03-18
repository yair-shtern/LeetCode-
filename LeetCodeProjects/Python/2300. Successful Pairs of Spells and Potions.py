# You are given two positive integer arrays spells and potions, of length n and m respectively,
# where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
#
# You are also given an integer success. A spell and potion pair is
# considered successful if the product of their strengths is at least success.
#
# Return an integer array pairs of length n where pairs[i] is the number of potions that will
# form a successful pair with the ith spell.
import bisect
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Bisect
        potions.sort()
        pairs = []
        m = len(potions)
        for spell in spells:
            minStrength = success // spell
            ind = bisect.bisect_left(potions, minStrength)
            pairs.append(m - ind)
        return pairs

        # Binary Search
        # def binarySearch(num):
        #     l, r = 0, len(potions)
        #     res = 0
        #     while l <= r:
        #         mid = l + (r - l) // 2
        #         if num * potions[mid] >= success:
        #             res += r - mid + 1
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        #     return res
        #
        # potions.sort()
        # resultArray = []
        # for s in spells:
        #     resultArray.append(binarySearch(s))
        # return resultArray
