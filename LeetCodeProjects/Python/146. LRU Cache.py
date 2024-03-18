# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise,
# add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation,
# evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.map = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.map.keys():
            self.map.move_to_end(key)
            return self.map[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map.keys():
            self.map.move_to_end(key)
        elif len(self.map) == self.capacity:
            self.map.popitem(last=False)
        self.map[key] = value

    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
