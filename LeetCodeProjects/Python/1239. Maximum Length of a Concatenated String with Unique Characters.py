# You are given an array of strings arr.
# A string s is formed by the concatenation of a subsequence of arr that has unique characters.
#
# Return the maximum possible length of s.
#
# A subsequence is an array that can be derived from another array by deleting some or no
# elements without changing the order of the remaining elements.
from typing import List


class Solution:
    def __init__(self):
        self.maxStrLen = float('-inf')

    def maxLength(self, arr: List[str]) -> int:
        def backtracking(curStr, ind):
            if ind == len(arr):
                self.maxStrLen = max(self.maxStrLen, len(curStr))
                return
            if all(arr[ind].count(c) + curStr.count(c) == 1 for c in arr[ind]):
                backtracking(curStr + arr[ind], ind + 1)
            backtracking(curStr, ind + 1)

        backtracking("", 0)
        return int(self.maxStrLen)
