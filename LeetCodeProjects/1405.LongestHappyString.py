# A string s is called happy if it satisfies the following conditions:
#
# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string.
# If there are multiple longest happy strings, return any of them.
# If there is no such string, return the empty string "".
#
# A substring is a contiguous sequence of characters within a string.
#
#
#
# Example 1:
#
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
# Example 2:
#
# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case.

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        abc_dict = {"a": a, "b": b, "c": c}

        res = ""
        while True:
            char = max(abc_dict.items(), key=lambda x: x[1])[0]
            count = abc_dict.pop(char)
            if count == 0:
                break

            if len(res) > 1 and res[-1] == res[-2] == char:
                char2, count2 = max(abc_dict.items(), key=lambda x: x[1])
                if count2 == 0:
                    break
                abc_dict[char2] -= 1
                res += char2
                abc_dict[char] = count

            else:
                res += char
                abc_dict[char] = count - 1

        return res


if __name__ == '__main__':
    print(Solution().longestDiverseString(1, 2, 7))
