from typing import List


class Solution:
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        visited = 0
        current = 0
        m = len(grid[0])
        for i, row in enumerate(grid, 0):
            for j, cell in enumerate(row, 0):
                # Wall
                if cell == -1:
                    visited |= 1 << (i * m + j)
                # Starting square
                if cell == 1:
                    current = i * m + j
                    visited |= 1 << (current)
        return self.helper(grid, visited, current)

    def helper(self, grid: List[List[int]], visited: int, current: int) -> int:
        n = len(grid)
        m = len(grid[0])
        i = current // m
        j = current % m
        # Already reached the end
        if grid[i][j] == 2:
            # Check if everything is visited
            if ((1 << n * m) - 1) == visited:
                return 1
            else:
                return 0

        res = 0
        for d in self.direction:
            if 0 <= i + d[0] and i + d[0] < n and 0 <= j + d[1] and j + d[1] < m:
                index = (i + d[0]) * m + j + d[1]
                if not visited & (1 << index):
                    visited |= 1 << index
                    res += self.helper(grid, visited, index)
                    visited &= ~(1 << index)
        return res


if __name__ == "__main__":
    grid = [[0, 1], [2, -1]]
    print(Solution().uniquePathsIII(grid))
