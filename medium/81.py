from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False

        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            while lo < hi and nums[lo] == nums[lo + 1]:
                lo += 1

            while lo < hi and nums[hi] == nums[hi - 1]:
                hi -= 1

            mid = (hi - lo) // 2 + lo
            if nums[mid] == target:
                return True

            if nums[mid] >= nums[lo]:
                # Mid in left array
                if target >= nums[lo] and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # Mid in right array
                if target <= nums[hi] and target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False
