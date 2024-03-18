# There are n cities numbered from 0 to n - 1 and n - 1 roads
# such that there is only one way to travel between two different cities (this network form a tree).
# Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.
#
# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
#
# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
#
# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
#
# It's guaranteed that each city can reach city 0 after reorder.
import collections
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(city):
            nonlocal visited, roadsMap, counter

            for neighbor, sign in roadsMap[city]:
                if not visited[neighbor]:
                    if sign == 1:
                        counter += 1
                    visited[neighbor] = True
                    dfs(neighbor)

        visited = [False] * n
        roadsMap = collections.defaultdict(list)
        for a, b in connections:
            roadsMap[a].append((b, 1))
            roadsMap[b].append((a, -1))

        counter = 0
        visited[0] = True
        dfs(0)
        return counter
