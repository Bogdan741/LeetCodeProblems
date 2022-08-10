from typing import List


class Solution:
    @staticmethod
    def rotateGrid(grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid[0])
        n = len(grid)
        mo = min(m, n) // 2
        mx = 0
        while mx < mo:
            # Copy the mx layer
            a = []
            i, j = mx, mx
            nn = n - mx
            mm = m - mx
            while i < nn:
                a.append(grid[i][j])
                i += 1
            i -= 1
            j += 1
            while j < mm:
                a.append(grid[i][j])
                j += 1
            j -= 1
            i -= 1
            while i >= mx:
                a.append(grid[i][j])
                i -= 1
            i += 1
            j -= 1
            while j >= mx + 1:
                a.append(grid[i][j])
                j -= 1
            # Rotate
            zl = k % len(a)
            a = a[len(a) - zl:] + a[: len(a) - zl]

            # Put it back
            kk = 0
            i, j = mx, mx
            while i < nn:
                grid[i][j] = a[kk]
                kk += 1
                i += 1
            i -= 1
            j += 1
            while j < mm:
                grid[i][j] = a[kk]
                kk += 1
                j += 1
            i -= 1
            j -= 1
            while i >= mx:
                grid[i][j] = a[kk]
                kk += 1
                i -= 1
            i += 1
            j -= 1
            while j >= mx + 1:
                grid[i][j] = a[kk]
                kk += 1
                j -= 1
            mx += 1
        return grid


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    k = int(input())
    grid = []
    for _ in range(n):
        grid_i = []
        for _ in range(m):
            grid_i.append(int(input()))
        grid.append(grid_i)

    print(Solution.rotateGrid(grid, k))
