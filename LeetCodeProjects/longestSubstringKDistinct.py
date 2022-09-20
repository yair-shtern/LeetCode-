import collections


class Solution(object):
    # Longest substring with at most K distinct characters
    def longestSubstring(self, string, k):
        """
        :type string: str
        :type k: int
        :rtype: int
        """
        if len(string) == 0 or k == 0:
            return 0

        left = right = 0
        result = 0

        chars_dict = collections.defaultdict(int)
        while right < len(string):
            r = string[right]
            chars_dict[r] += 1

            while len(chars_dict) > k:
                l = string[left]
                if chars_dict[l] == 1:
                    chars_dict.pop(l)
                else:
                    chars_dict[l] -= 1
                left += 1

            result = max(result, right - left + 1)
            right += 1

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestSubstring("eceba", 2) == 3)
    print(sol.longestSubstring("aa", 1) == 2)
    print(sol.longestSubstring("ecebaa", 2) == 3)
    print(sol.longestSubstring("aabacccac", 2) == 6)
    print(sol.longestSubstring("aabacccac", 1) == 3)
