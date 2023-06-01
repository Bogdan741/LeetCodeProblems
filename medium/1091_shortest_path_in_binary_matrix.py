from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        directions = [
            (1, 0), (-1, 0), (0, 1),
            (0, -1), (1, 1), (1, -1),
            (-1, 1), (-1, -1),
        ]

        m = len(grid)
        n = len(grid[0])
        d = deque()
        d.append((0, 0))
        grid[0][0] = -1

        # BFS
        while len(d) > 0:
            (i, j) = d.pop()
            distance = -grid[i][j] + 1
            for vec_i, vec_j in directions:
                if (i + vec_i < m and i + vec_i >= 0) and (j + vec_j < n and j + vec_j >= 0) and grid[i + vec_i][j + vec_j] == 0:
                    d.appendleft((i + vec_i, j + vec_j))
                    grid[i + vec_i][j + vec_j] = -distance

        if grid[-1][-1] == 0:
            return -1
        return -grid[-1][-1]
