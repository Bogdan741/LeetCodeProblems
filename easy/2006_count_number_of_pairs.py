from typing import List
from collections import Counter


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        uniqueNums = list(set(nums))
        uniqueNums.sort()
        if len(nums) == 1:
            return 0
        first = 0
        second = 1
        counter = 0
        while(second < len(uniqueNums)):
            if abs(uniqueNums[second] - uniqueNums[first]) == k:
                counter += c[uniqueNums[second]] * c[uniqueNums[first]]
                second += 1
                first += 1
            elif abs(uniqueNums[second] - uniqueNums[first]) < k:
                second += 1
            elif abs(uniqueNums[second] - uniqueNums[first]) > k:
                first += 1

        return counter
