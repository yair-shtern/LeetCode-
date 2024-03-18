# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; there are no extra white spaces,
# square brackets are well-formed, etc. Furthermore,
# you may assume that the original data does not contain any digits and that digits are only for those repeat numbers,
# k. For example, there will not be input like 3a or 2[4].
#
# The test cases are generated so that the length of the output will never exceed 105.
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                tmpStr = ''
                while stack[-1] != '[':
                    tmpStr = stack.pop() + tmpStr
                stack.pop()  # remove '['
                digit = stack.pop()
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                stack.append(int(digit) * tmpStr)
        return ''.join(stack)
