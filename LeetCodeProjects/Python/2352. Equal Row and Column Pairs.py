# Given a 0-indexed n x n integer matrix grid,
# return the number of pairs (ri, cj) such that row ri and column cj are equal.
#
# A row and column pair is considered equal if they contain the same elements
# in the same order (i.e., an equal array).
import collections
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = collections.defaultdict(int)
        for row in grid:
            d[tuple(row)] += 1
        numEqualPairs = 0
        for row in zip(*grid):
            numEqualPairs += d[tuple(row)]
        return numEqualPairs

# class Solution:
#     def equalPairs(self, grid: List[List[int]]) -> int:
#         numEqualPairs = 0
#         gridT = [list(i) for i in zip(*grid)]
#         for row in grid:
#             if row in gridT:
#                 numEqualPairs += gridT.count(row)
#
#         return numEqualPairs
