# You are given an array of variable pairs equations and an array of real numbers values,
# where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].
# Each Ai or Bi is a string that represents a single variable.
#
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query
# where you must find the answer for Cj / Dj = ?.
#
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
#
# Note: The input is always valid. You may assume that evaluating the queries
# will not result in division by zero and that there is no contradiction.
#
# Note: The variables that do not occur in the list of equations are undefined,
# so the answer cannot be determined for them.
import collections
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # DFS:
        #
        # equationsMap = collections.defaultdict(dict)
        # for i, (a, b) in enumerate(equations):
        #     equationsMap[a][b] = values[i]
        #     equationsMap[b][a] = 1 / values[i]
        #
        # def dfs(src, target, visited):
        #     if src not in equationsMap or target not in equationsMap:
        #         return -1.0
        #
        #     if target in equationsMap[src]:
        #         return equationsMap[src][target]
        #     for nei in equationsMap[src]:
        #         if nei not in visited:
        #             visited.add(nei)
        #             tmp = dfs(nei, target, visited)
        #             if tmp == -1.0:
        #                 continue  # to next neighbors
        #             else:
        #                 return tmp * equationsMap[src][nei]
        #     return -1.0
        #
        # return [dfs(q[0], q[1],set()) for q in queries]

        # BFS:
        equationsMap = collections.defaultdict(list)
        for i, (a, b) in enumerate(equations):
            equationsMap[a].append((b, values[i]))
            equationsMap[b].append((a, 1 / values[i]))

        def bfs(x, y):
            if x not in equationsMap or y not in equationsMap:
                return -1.0

            queue, visited = collections.deque(), set()
            queue.append([x, 1.0])
            visited.add(x)
            while queue:
                a, val = queue.popleft()
                if a == y:
                    return val
                for b, result in equationsMap[a]:
                    if b not in visited:
                        queue.append([b, result * val])
                        visited.add(b)
            return -1.0

        return [bfs(x, y) for x, y in queries]
