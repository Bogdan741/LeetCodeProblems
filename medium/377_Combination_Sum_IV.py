from typing import List
from math import factorial
from functools import reduce


# Brute force
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.nums = sorted(nums)
        self.target = target
        return self.helpFunction(0, 0, [])

    def helpFunction(self, usum: int, index: int, used: List[int]) -> int:
        if usum >= self.target or index >= len(self.nums):
            if usum == self.target:
                total = sum(used, 0)
                return int(
                    reduce(lambda y, x: y / factorial(x), used, factorial(total))
                )
            return 0
        res = self.helpFunction(usum, index + 1, used.copy())
        i = 0
        while usum < self.target:
            i += 1
            usum += self.nums[index]
            temp_used = used.copy()
            temp_used.append(i)
            res += self.helpFunction(usum, index + 1, temp_used)
        return res


# Dynamic programming
class Solution1:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        dp[0] = [1]

        def search(curtarget):
            if curtarget < 0:
                return 0
            if curtarget in dp:
                return dp[curtarget]
            comb_sum = 0
            for num in nums:
                if curtarget > num:
                    comb_sum += search(curtarget - num)
                elif curtarget == num:
                    comb_sum += 1
            dp[curtarget] = comb_sum
            return comb_sum

        return search(target)


if __name__ == "__main__":
    print(Solution().combinationSum4([1, 2, 3], 4))
