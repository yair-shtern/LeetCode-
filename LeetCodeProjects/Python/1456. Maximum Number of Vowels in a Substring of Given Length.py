# Given a string s and an integer k,
# return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        maxNumVowels = tmpNumVowels = sum(1 for v in s[:k] if v in vowels)
        l, r = 0, k
        while r < len(s):
            tmpNumVowels -= 1 if s[l] in vowels else 0
            tmpNumVowels += 1 if s[r] in vowels else 0
            maxNumVowels = tmpNumVowels if tmpNumVowels > maxNumVowels else maxNumVowels
            l, r = l + 1, r + 1
        return maxNumVowels
