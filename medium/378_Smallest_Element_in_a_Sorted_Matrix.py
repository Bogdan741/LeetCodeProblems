from typing import List
import bisect


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n = len(matrix)
        low, high = matrix[0][0], matrix[-1][-1]

        while low < high:
            mid = (low + high) // 2
            count = 0
            for i in range(n):
                index = bisect.bisect_right(matrix[i], mid)
                if index == 0:
                    break
                count += index
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low


# import numpy as np
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int):
#         n = len(matrix)
#         last, sy, sx = self.evaluate(n, k - 1)
#         nth = k - 1 - last
#         res = []
#         while sx < n and sy >= 0:
#             res.append(matrix[sy][sx])
#             sx += 1
#             sy -= 1
#         pr = np.partition(res, nth)
#         return pr[nth]
#
#     def evaluate(self, n, k):
#         i = j = start_index = counter = 0
#         end_index = -1
#         while i < n:
#             start_index = end_index + 1
#             end_index = start_index + i
#             if start_index <= k and k <= end_index:
#                 return (start_index, i, j)
#             i += 1
#         i -= 1
#
#         j += 1
#         while j < n:
#             start_index = end_index + 1
#             end_index = start_index + n - j - 1
#             if start_index <= k and k <= end_index:
#                 return (start_index, i, j)
#             j += 1
#         j -= 1
#
#         return (start_index, i, j)
