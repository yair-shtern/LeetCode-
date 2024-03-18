# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        for i in range(min(len1, len2), 0, -1):
            if len1 % i == 0 and len2 % i == 0 and \
                    str1[:i] * (len1 // i) == str1 and str1[:i] * (len2 // i) == str2:
                return str1[:i]
        return ""

