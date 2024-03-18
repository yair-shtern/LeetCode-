# Given an array of integers arr,
# return true if the number of occurrences of each value in the array is unique or false otherwise.
from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return len(counter) == len(set(counter.values()))
