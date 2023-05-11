# Given an integer array nums, return true if there exists a triple of indices
# (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
# indices exists, return false.

from typing import List
import math


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        c1 = math.inf
        c2 = math.inf
        for i in nums:
            if i <= c1:
                c1 = i
            elif i <= c2:
                c2 = i
            else:
                return True
        return False
