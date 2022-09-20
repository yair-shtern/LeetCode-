# For example given string S = aBBaabb, the blocks are: 'a', 'BB', 'aa' and 'bb'.
# Write a function that given string S, returns the minimal number of characters
# needed to make all blocks equal in length.
#
# For example:
# S = abaabb, return: 2 -> aabbaabb

class Solution(object):
    def minCharsToAdd(self, s):
        if len(s) == 0:
            return 0

        max_block_length = 1
        curr_block_length = 1
        num_of_blocks = 1
        current_char = s[0]

        for i in range(1, len(s)):
            if s[i] != current_char:
                max_block_length = max(curr_block_length, max_block_length)
                current_char = s[i]
                num_of_blocks += 1
                curr_block_length = 1
            else:
                curr_block_length += 1

        expected_length = num_of_blocks * max_block_length
        return expected_length - len(s)


if __name__ == '__main__':
    print(Solution().minCharsToAdd("aBBaa") == 1)
    print(Solution().minCharsToAdd("aaBBBaa") == 2)
    print(Solution().minCharsToAdd("aBBBaa") == 3)
    print(Solution().minCharsToAdd("aaaBBBaaa") == 0)
