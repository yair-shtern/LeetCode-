# You are given two strings word1 and word2. Merge the strings by adding letters
# in alternating order, starting with word1. If a string is longer than the other,
# append the additional letters onto the end of the merged string.
#
# Return the merged string.
#
#
#
# Example 1:
#
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:
#
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:
#
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        longer, shorter = (word1, word2) if len(word1) >= len(word2) else (word2, word1)
        return "".join([word1[i] + word2[i] for i in range(len(shorter))]) + longer[len(shorter):]

        # res = ""
        # len1, len2 = len(word1), len(word2)
        #
        # for i in range(min(len1, len2)):
        #     res += word1[i] + wrd2[i]
        #
        # if len1 < len2:
        #     res += word2[len1:]
        #
        # elif len2 < len1:
        #     res += word1[len2:]
        #
        # return res


if __name__ == '__main__':
    print(Solution().mergeAlternately("ab", "pqrs"))
