# You are given an m x n grid where each cell can have one of three values:
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1.
import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = {(0, 1), (1, 0), (0, -1), (-1, 0)}
        queue = collections.deque()
        m, n = len(grid), len(grid[0])
        numFreshOranges = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                elif grid[row][col] == 1:
                    numFreshOranges += 1
        minute = 0
        while queue:
            row, col, layer = queue.popleft()
            for dr, dc in direction:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                    grid[r][c] = 2
                    numFreshOranges -= 1
                    queue.append((r, c, layer + 1))
            minute = layer
        return minute if numFreshOranges == 0 else -1
