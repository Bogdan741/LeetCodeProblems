# Hard
# You are given an integer array nums and you have to return a new counts array.
# The counts array has the property where counts[i] is the number of smaller
# elements to the right of nums[i].
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.nums = [[i,nums[i]] for i in range(len(nums))]
        self.counts = [0 for _ in range(len(nums))]
        self.mergeSort(0, len(nums) - 1)
        return self.counts

    def mergeSort(self, start : int, end):
        if(start < end):
            m = (start + end) // 2
            self.mergeSort(start, m)
            self.mergeSort(m + 1, end)
            self.merge(start,m, end)

    def merge(self,s: int, m: int, e: int):
        n1 = m - s + 1
        n2 = e - m
        L = [self.nums[i + s] for i in range(n1)]
        R = [self.nums[i + m + 1] for i in range(n2)]
        i = j = 0
        count = 0 
        for k in range(s, e + 1):
            if i < n1 and j < n2:
                if L[i][1] <= R[j][1]:
                    idx = L[i][0]
                    self.counts[idx] += count
                    self.nums[k] = L[i]
                    i+=1
                else:
                    count+=1
                    self.nums[k] = R[j]
                    j+=1
            elif j < n2:
                count+=1
                self.nums[k] = R[j]
                j+=1
            elif i < n1:
                idx=L[i][0]
                self.counts[idx] += count
                self.nums[k] = L[i]
                i+=1

# Test
if __name__=='__main__':
    print(Solution().countSmaller([5,2,6,1]))
