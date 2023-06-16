from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        nums.sort()
        left = 0
        right = 0
        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[right] == 1:
                right = i
            else:
                res.append((nums[left], nums[right]))
                left = i
                right = i

        res.append((nums[left], nums[right]))
        return list(map(lambda x: Solution.helper(x[0], x[1]), res))

    @staticmethod
    def helper(a, b):
        if a == b:
            return str(a)
        else:
            return f"{a}->{b}"
