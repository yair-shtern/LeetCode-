# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the
# non-overlapping intervals that cover all the intervals in the input.
#
#
#
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = res[-1][1]
            # Check if the last interval we added ends after the next interval starts
            if last_end >= start:
                res[-1][1] = max(last_end, end)
            else:
                res.append([start, end])

        return res


if __name__ == '__main__':
    print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
