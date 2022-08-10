class Solution:
    def findPaths( self, n: int, m: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self._n = n
        self._m = m
        self.memoize_table = [ [[-1 for _ in range(maxMove + 1)] for _ in range(m)] for _ in range(n) ]
        return self.f(startRow, startColumn, maxMove) % (10**9 + 7)

    def f(self, i: int, j: int, k: int) -> int:
        if k == 0:
            return 0
        key = self.memoize_table[i][j][k]
        if key == -1:
            paths = 0
            # Check for bounderies
            # Row boundaries
            if i == 0:
                paths += 1
            if i == self._n - 1:
                paths += 1

            # Column boundaries
            if j == 0:
                paths += 1
            if j == self._m - 1:
                paths += 1

            # Find for adjacent cells
            if i > 0:
                paths += self.f(i - 1, j, k - 1)
            if i < self._n - 1:
                paths += self.f(i + 1, j, k - 1)
            if j > 0:
                paths += self.f(i, j - 1, k - 1)
            if j < self._m - 1:
                paths += self.f(i, j + 1, k - 1)

            self.memoize_table[i][j][k] = paths
            return paths
        return key

