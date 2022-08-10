from typing import List
from bisect import bisect_right, bisect_left


# Prefix sum + binary search
# Space: O(n), Time: O(nlogn)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = []
        sum = 0
        for i in nums:
            sum += i
            prefix.append(sum)

        min_length = int('inf')
        for i in range(len(prefix)):
            if prefix[i] >= target:
                index = bisect_right(prefix, prefix[i] - target)
                min_length = min(min_length, i - index + 1)
        return 0 if min_length == int('inf') else min_length


# Sliding window with two pointers
# Space: O(1). Time: O(n)
class Solution1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        smallest = int("inf")
        start = windowSum = 0

        for end in range(len(nums)):
            windowSum += nums[end]
            while windowSum >= target:
                smallest = min(smallest, end - start + 1)
                windowSum -= nums[start]
                start += 1

        return smallest if smallest != float("inf") else 0


class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        start = end = 0
        counter = nums[0]
        minimumLength = int("inf")

        while end < len(nums):
            if counter >= target:
                minimumLength = min(minimumLength, end - start + 1)
                counter -= nums[start]
                start += 1

            else:
                end += 1
                if end <= (len(nums) - 1):
                    counter += nums[end]

        return 0 if minimumLength == int("inf") else minimumLength
