# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
#
# Implement the SmallestInfiniteSet class:
#
# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set,
# if it is not already in the infinite set.
import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.addedHeap = []
        heapq.heapify(self.addedHeap)
        self.curMin = 1

    def popSmallest(self) -> int:
        if self.addedHeap:
            return heapq.heappop(self.addedHeap)
        self.curMin += 1
        return self.curMin - 1

    def addBack(self, num: int) -> None:
        if num < self.curMin and num not in self.addedHeap:
            heapq.heappush(self.addedHeap, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
