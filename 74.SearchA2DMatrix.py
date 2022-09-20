# Write an efficient algorithm that searches for a value target in an m x n
# integer matrix matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
#
#
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if matrix[0][0] > target:
            return False

        m, n = len(matrix), len(matrix[0])
        start, end = 0, m - 1
        while start <= end:
            mid_row = (start + end) // 2
            if matrix[mid_row][-1] < target:
                start = mid_row + 1
            elif matrix[mid_row][0] > target:
                end = mid_row - 1
            else:
                break

        if not start <= end:
            return False

        row = (start + end) // 2
        l, mid, r = 0, 0, n - 1
        while l <= r:
            mid = (r + l) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        return False


if __name__ == '__main__':
    print(Solution().searchMatrix([[1, 1]], 2))
