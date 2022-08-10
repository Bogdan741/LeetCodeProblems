# Write an efficient algorithm that searches for a value target in an m x n
# integer matrix matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right. Integers in
# each column are sorted in ascending from top to bottom.
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = False
        row, col = len(matrix) -1 , 0
        while row >= 0 and col < len(matrix[0]):
            if(target<matrix[row][col]):
                row-=1
            elif(target>matrix[row][col]):
                col-=1
            else:
                res = True
        return res

if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    target = 20
    print(Solution().searchMatrix(matrix, target))
