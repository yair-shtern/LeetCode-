# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.')
# and walls (represented as '+'). You are also given the entrance of the maze,
# where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.
#
# In one step, you can move one cell up, down, left, or right.
# You cannot step into a cell with a wall, and you cannot step outside the maze.
# Your goal is to find the nearest exit from the entrance.
# An exit is defined as an empty cell that is at the border of the maze.
# The entrance does not count as an exit.
#
# Return the number of steps in the shortest path from the entrance to the nearest exit,
# or -1 if no such path exists.
import collections
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}
        queue = collections.deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'

        while queue:
            row, col, distance = queue.popleft()
            if (row == 0 or row == m - 1 or col == 0 or col == n - 1) and distance > 0:
                return distance

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and maze[r][c] == '.':
                    queue.append((r, c, distance + 1))
                    maze[r][c] = '+'

        return -1
# class Solution:
#     def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
#         m, n = len(maze), len(maze[0])
#         directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}
#         queue = collections.deque([(entrance[0], entrance[1], 0)])
#         visited = [[False] * n for _ in range(m)]
#         visited[entrance[0]][entrance[1]] = True
#
#         while queue:
#             row, col, distance = queue.popleft()
#             if (row == 0 or row == m - 1 or col == 0 or col == n - 1) and distance > 0:
#                 return distance
#
#             for dr, dc in directions:
#                 r, c = row + dr, col + dc
#                 if 0 <= r < m and 0 <= c < n and maze[r][c] == '.' and not visited[r][c]:
#                     queue.append((r, c, distance + 1))
#                     visited[r][c] = True
#
#         return -1
