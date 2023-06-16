from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_dict = {}
        for i in range(n):
            key = hash(tuple(grid[i]))
            if key in row_dict:
                row_dict[key] += 1
            else:
                row_dict[key] = 1

        col_dict = {}
        for i in range(n):
            key = hash(tuple(map(lambda j: j[i], grid)))
            if key in col_dict:
                col_dict[key] += 1
            else:
                col_dict[key] = 1

        sum = 0
        for key in row_dict.keys():
            if key in col_dict:
                sum += row_dict[key] * col_dict[key]
        return sum
