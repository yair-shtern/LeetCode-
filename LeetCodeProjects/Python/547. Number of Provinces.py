# There are n cities. Some of them are connected, while some are not.
# If city a is connected directly with city b, and city b is connected directly with city c,
# then city a is connected indirectly with city c.
#
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
#
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city
# and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
#
# Return the total number of provinces.
import collections
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected[0])
        visited = [False] * n
        count = 0

        def bfs(start):
            queue = collections.deque([start])
            visited[start] = True
            while queue:
                c = queue.popleft()
                for j in range(0, n):
                    if isConnected[c][j] and not visited[j]:
                        queue.append(j)
                        visited[j] = True

        for i in range(n):
            if not visited[i]:
                bfs(i)
                count += 1

        return count
