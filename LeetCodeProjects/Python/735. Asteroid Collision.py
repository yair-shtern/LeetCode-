# We are given an array asteroids of integers representing asteroids in a row.
#
# For each asteroid, the absolute value represents its size,
# and the sign represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions.
# If two asteroids meet, the smaller one will explode.
# If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                diff = ast + stack[-1]
                if diff < 0:
                    stack.pop()
                    continue
                if diff == 0:
                    stack.pop()
                break
            else:
                stack.append(ast)
        return stack