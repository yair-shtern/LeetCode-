# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's,
# where 0 means empty and 1 means not empty, and an integer n,
# return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        numPlanted = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and  (i==len(flowerbed)-1 or flowerbed[i + 1] == 0):
                numPlanted += 1
                i += 1
            elif flowerbed[i] == 1:
                i += 1
            i += 1
        return numPlanted >= n
