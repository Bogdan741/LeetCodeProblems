from functools import lru_cache


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))

        def isValidCell(row, col) -> bool:
            return (row >= 0 and row < n) and (col >= 0 and col < n)

        @lru_cache(maxsize=None)
        def solve(depth: int, row: int, col: int) -> float:
            if depth == k:
                return (1 / 8) ** (depth)

            res = 0
            for row_offset, col_offset in dirs:
                if isValidCell(row + row_offset, col + col_offset):
                    res += solve(depth + 1, row + row_offset, col + col_offset)
            return res

        return solve(0, row, column)


# Some compute optimize solution, but it will be slower
# since python whould not use a dynamic bitmap
class Solution1:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))

        multiplier = 1 << 3 * k

        def isValidCell(row, col) -> bool:
            return (row >= 0 and row < n) and (col >= 0 and col < n)

        @lru_cache(maxsize=None)
        def solve(depth: int, row: int, col: int) -> float:
            if depth == k:
                return multiplier >> 3 ** (depth)

            res = 0
            for row_offset, col_offset in dirs:
                if isValidCell(row + row_offset, col + col_offset):
                    res += solve(depth + 1, row + row_offset, col + col_offset)
            return res

        return solve(0, row, column) / multiplier
