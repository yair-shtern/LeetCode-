# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
#
# You must do it in place.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:
#
#
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(1) space solution!
        rows_num, cols_num = len(matrix), len(matrix[0])

        # Indicates if first row or column should be set to zeros
        first_row = first_col = False
        for i in range(cols_num):
            if matrix[0][i] == 0:
                first_row = True
                break
        for i in range(rows_num):
            if matrix[i][0] == 0:
                first_col = True
                break

        # Go throw the matrix and set the first row and column to zeros in the
        # indexes were there is a zero in the co-responding column or row
        for row in range(rows_num):
            for col in range(cols_num):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        # Set to zero the indexes according to the first row and column
        for row in range(1, rows_num):
            for col in range(1, cols_num):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        # Finally update the first row and column
        if first_row:
            for i in range(cols_num):
                matrix[0][i] = 0

        if first_col:
            for i in range(rows_num):
                matrix[i][0] = 0


if __name__ == '__main__':
    mat = [[0, 1, 2, 0],
           [3, 4, 5, 2],
           [1, 3, 1, 5]]
    Solution().setZeroes(mat)
    print(mat)
