# You are given an array of strings arr. A string s is formed by the
# concatenation of a subsequence of arr that has unique characters.
#
# Return the maximum possible length of s.
#
# A subsequence is an array that can be derived from another array by deleting
# some or no elements without changing the order of the remaining elements.
#
#
#
# Example 1:
#
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.
# Example 2:
#
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible longest valid concatenations are
# "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
# Example 3:
#
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# Explanation: The only string in arr has all 26 characters.

class Solution(object):
    # Maximum Length of a Concatenated String with Unique Characters
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """

        # the recursive function
        def recurse(s, i):
            if i >= n:  # if we reach to the end of the array update to the maximum
                self.answer = max(self.answer, len(s))
                return

            # the recursive call with and without arr[i]
            recurse(s, i + 1)
            ans = s + arr[i]
            if len(ans) == len(set(ans)):  # if ans legal call to the function
                recurse(ans, i + 1)

        # initializations
        n = len(arr)
        self.answer = 0
        recurse("", 0)
        return self.answer  # in the end return the updated answer
