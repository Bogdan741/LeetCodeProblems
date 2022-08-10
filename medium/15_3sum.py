# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j]
# + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.

# TAG: Two pointers, Sorting
from typing import List
import bisect


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            left = i + 1
            right = n - 1
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    res.append((nums[i], nums[right], nums[left]))
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res
