from typing import List


# Not a solution just some thoghts, the real solution in [174.cpp]
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = {}
        dp[(m - 1, n - 1)] = dungeon[m - 1][n - 1]
        # Last row
        for i in range(n - 2, -1, -1):
            dp[(m - 1, i)] = dp[(m - 1, i + 1)] + dungeon[m - 1][i]

        # Last col
        for i in range(m - 2, -1, -1):
            dp[(i, n - 1)] = dp[(i + 1, n - 1)] + dungeon[i][n - 1]

        i = m - 2
        j = n - 2
        while i >= 0 or j >= 0:
            # Do
            # Update row
            for k in range(j, -1, -1):
                dp[(i, k)] = max(dp[(i + 1, k), dp[(i, k + 1)]]) + dungeon[i][k]
            for z in range(i, -1, -1):
                dp[(z, j)] = max(dp[(z + 1, j), dp[(z, j + 1)]]) + dungeon[z][j]
            # Update col

            # Update
            i -= 1
            j -= 1
        return -dp[(0, 0)]
