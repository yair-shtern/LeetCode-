# Given a string s, return the number of palindromic substrings in it.
#
# A string is a palindrome when it reads the same backward as forward.
#
# A substring is a contiguous sequence of characters within the string.
#
#
#
# Example 1:
#
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
#
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # odd length palindrome
            l = r = i
            res = self.count_palindrome(l, r, res, s)

            # even length palindrome
            l, r = i, i + 1
            res = self.count_palindrome(l, r, res, s)
        return res

    def count_palindrome(self, l, r, res, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res


if __name__ == '__main__':
    Solution().countSubstrings("aaaa")