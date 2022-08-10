# There is a robot on an m x n grid. The robot is initially located at the
# top-left corner (i.e., grid[0][0]). The robot tries to move to the
# bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
# either down or right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths
# that the robot can take to reach the bottom-right corner.
#
# The test cases are generated so that the answer will be less than or equal to
# 2 * 109
from math import comb


# Math solution (much faster)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, m - 1)


# Dynamic programming solution (intuitive)
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        sum = 0
        if m > 1:
            sum += self.uniquePaths(m - 1, n)
        else:
            return 1
        if n > 1:
            sum += self.uniquePaths(m, n - 1)
        else:
            return 1
        return sum
