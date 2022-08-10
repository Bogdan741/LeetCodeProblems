from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dict = {}
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                val = nums[i] * nums[j]
                prev = dict.get(val, False)
                dict[val] = prev + 1 if prev else 1
        return sum([4 * x * (x - 1) for x in dict.values()])


# Test
if __name__ == "__main__":
    print(Solution().tupleSameProduct([2, 3, 4, 6, 8, 12]))
