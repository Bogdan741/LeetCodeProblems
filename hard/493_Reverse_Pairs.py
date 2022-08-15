from typing import List
import bisect
import heapq


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.nums = nums
        self.count = 0
        self.mergeSort(0, len(nums) - 1)
        return self.count

    def mergeSort(self, start: int, end):
        if start < end:
            m = (start + end) // 2
            self.mergeSort(start, m)
            self.mergeSort(m + 1, end)
            self.merge(start, m, end)

    def merge(self, s: int, m: int, e: int):
        n1 = m - s + 1
        n2 = e - m
        L = [self.nums[i + s] for i in range(n1)]
        R = [self.nums[i + m + 1] for i in range(n2)]
        i = j = 0

        for b in range(n2):
            key = R[b] * 2
            idx = bisect.bisect_right(L, key)
            self.count += n1 - idx

        for k in range(s, e + 1):
            if i < n1 and j < n2:
                if L[i] <= R[j]:
                    # self.count += count
                    self.nums[k] = L[i]
                    i += 1
                else:
                    # idx = bisect.bisect_right(L, 2 * R[j], lo=i)
                    # count += 1
                    # self.count -= idx - i
                    self.nums[k] = R[j]
                    j += 1
            elif j < n2:
                self.nums[k] = R[j]
                j += 1
            elif i < n1:
                # self.count += count
                self.nums[k] = L[i]
                i += 1
        # self.nums[s:e] = heapq.merge(L, R)


if __name__ == "__main__":
    print(Solution().reversePairs([313, 165, -364, 46, 328, 432, 47]))
