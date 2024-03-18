# You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:
#
# Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
# Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
# Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
# Given the integer n, return the last number that remains in arr.
from collections import deque


class Solution:
    def lastRemaining(self, n: int) -> int:
        arr = [1] * n
        numsRemain = n
        goRight = True
        k, jump = 0, 2
        while numsRemain > 1:
            print(arr)
            if k >= n:
                goRight = False
                jump *= 2
                k = n - 1
                while arr[k] == -1: k -= 1
            elif k < 0:
                goRight = True
                jump *= 2
                k = 0
                while arr[k] == -1: k += 1
            else:
                arr[k] = -1
                k = k + jump if goRight else k - jump
                numsRemain -= 1

        return next(i + 1 for i in range(n) if arr[i] != -1)
