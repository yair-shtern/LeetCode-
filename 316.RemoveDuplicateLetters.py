# Given a string s, remove duplicate letters so that every letter appears once
# and only once. You must make sure your result is the smallest in lexicographical
# order among all possible results.
#
#
#
# Example 1:
#
# Input: s = "bcabc"
# Output: "abc"
# Example 2:
#
# Input: s = "cbacdcbc"
# Output: "acdb"
import collections
from string import ascii_lowercase


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        chars_count = collections.Counter(s)
        stack = []
        seen = set()

        for c in s:
            chars_count[c] -= 1
            if c in seen:
                continue
            while stack and stack[-1] > c and chars_count[stack[-1]] > 0:
                s = stack.pop()
                seen.remove(s)
            stack.append(c)
            seen.add(c)

        return "".join(stack)


if __name__ == '__main__':
    print(Solution().removeDuplicateLetters("bcabc"))
    print(Solution().removeDuplicateLetters("cbacdcbc"))
