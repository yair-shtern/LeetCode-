# Find all valid combinations of k numbers that sum up to n
# such that the following conditions are true:
#
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain
# the same combination twice, and the combinations may be returned in any order.
import itertools
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # nums = [i for i in range(1, 9 + 1)]
        #
        # combinations = itertools.combinations(nums, k)
        #
        # return [comb for comb in combinations if sum(comb) == n]

        res = []

        def backtrack(nCur, start, curComb):
            if k == len(curComb):
                if nCur == n:
                    res.append(curComb)
                return
            for i in range(start, 10):
                backtrack(nCur + i, i + 1, curComb + [i])

        backtrack(0, 1, [])
        return res
