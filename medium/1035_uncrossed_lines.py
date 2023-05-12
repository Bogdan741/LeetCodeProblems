# You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.
#
# We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:
#
#     nums1[i] == nums2[j], and
#     the line we draw does not intersect any other connecting (non-horizontal) line.
#
# Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).
#
# Return the maximum number of connecting lines we can draw in this way.

# Let brute force it
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)

        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[n1][n2]
