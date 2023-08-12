from typing import List
from functools import lru_cache


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        @lru_cache(maxsize=None)
        def solve(i, j):
            if i == m - 1 and j == n - 1 and obstacleGrid[i][j] != 1:
                return 1
            if not ((i >= 0 and i < m) and (j >= 0 and j < n)):
                return 0

            if obstacleGrid[i][j] == 1:
                return 0
            else:
                return solve(i + 1, j) + solve(i, j + 1)

        return solve(0, 0)
