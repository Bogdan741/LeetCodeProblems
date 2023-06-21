from typing import List
from functools import reduce


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in range(m)]

        mod = 1_000_000_000 + 7

        def solve(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            sum = 1
            for dir_i, dir_j in directions:
                if (
                    dir_i + i >= 0
                    and dir_i + i < m
                    and dir_j + j >= 0
                    and dir_j + j < n
                    and grid[dir_i + i][dir_j + j] > grid[i][j]
                ):
                    sum += solve(dir_i + i, dir_j + j) % mod

            dp[i][j] = sum % mod
            return sum

        return sum(solve(i, j) for i in range(m) for j in range(n)) % mod
