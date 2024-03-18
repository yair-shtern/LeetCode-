# 387. First Unique Character in a String
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        charsMap = collections.Counter(s)
        for i in range(len(s)):
            if charsMap[s[i]]==1:
                return i
        return -1