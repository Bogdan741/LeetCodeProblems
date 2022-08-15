# A matrix diagonal is a diagonal line of cells starting from some cell in either
# the topmost row or leftmost column and going in the bottom-right direction
# until reaching the matrix's end. For example, the matrix diagonal starting from
# mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1],
# and mat[4][2].
#
# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending
# order and return the resulting matrix.

from typing import Tuple, List


# Sort in place with merge sort
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        self.mat = mat
        self.n = len(mat)
        self.m = len(mat[0])
        for i in range(self.m):
            self.mergeSort(
                (0, i), (min(self.n, self.m - i) - 1, i + min(self.n, self.m - i) - 1)
            )
        for i in range(1, self.n):
            self.mergeSort(
                # (i, 0), (min(self.n - i, self.m) - 1, min(self.n - i, self.m) - 1)
                (i, 0),
                (i + min(self.n - i, self.m) - 1, min(self.n - i, self.m) - 1),
            )
        return self.mat

    def mergeSort(self, start: Tuple[int, int], end: Tuple[int, int]):
        if start < end:
            m = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
            self.mergeSort(start, m)
            self.mergeSort((m[0] + 1, m[1] + 1), end)
            self.merge(start, m, end)

    def merge(self, s: Tuple[int, int], m: Tuple[int, int], e: Tuple[int, int]):
        n1 = m[0] - s[0] + 1
        n2 = e[0] - m[0]
        L = [self.mat[s[0] + i][s[1] + i] for i in range(n1)]
        R = [self.mat[m[0] + i + 1][m[1] + i + 1] for i in range(n2)]
        i = j = 0

        for k in range(s[0], e[0] + 1):
            if i < n1 and j < n2:
                if L[i] <= R[j]:
                    self.mat[k][s[1] + k - s[0]] = L[i]
                    i += 1
                else:
                    self.mat[k][s[1] + k - s[0]] = R[j]
                    j += 1
            elif j < n2:
                self.mat[k][s[1] + k - s[0]] = R[j]
                j += 1
            elif i < n1:
                self.mat[k][s[1] + k - s[0]] = L[i]
                i += 1


# Faster in python, shouldnt be general case, because copies is time consuming
class Solution1:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        total_num = row * col

        for i in range(1, row + col - 2):
            if i < row:
                start_row, start_col = row - i - 1, 0
            else:
                start_row, start_col = 0, i - row + 1

            diag = []
            while start_row < row and start_col < col:
                diag.append(mat[start_row][start_col])
                start_row += 1
                start_col += 1

            diag.sort()
            start_row -= 1
            start_col -= 1
            while start_row >= 0 and start_col >= 0:
                mat[start_row][start_col] = diag.pop()
                start_row -= 1
                start_col -= 1

        return mat
