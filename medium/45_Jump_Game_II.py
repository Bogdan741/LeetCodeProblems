from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        n = len(nums)
        cur = n - 1
        idx = n - 1
        hops = 0
        while True:
            for i in range(cur, -1, -1):
                if nums[i] + i >= cur:
                    idx = i
            cur = idx
            hops += 1
            if idx == 0:
                break

        return hops


class Solution1:
    def jump(self, nums: List[int]) -> int:
        # The starting range of the first jump is [0, 0]
        answer, n = 0, len(nums)
        cur_end, cur_far = 0, 0
        
        for i in range(n - 1):
            # Update the farthest reachable index of this jump.
            cur_far = max(cur_far, i + nums[i])

            # If we finish the starting range of this jump,
            # Move on to the starting range of the next jump.
            if i == cur_end:
                answer += 1
                cur_end = cur_far
                
        return answer
