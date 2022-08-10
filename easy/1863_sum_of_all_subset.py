# The XOR total of an array is defined as the bitwise XOR of all its elements,
# or 0 if the array is empty.
#
# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1. Given
# an array nums, return the sum of all XOR totals for every subset of nums. 
#
# Note: Subsets with the same elements should be counted multiple times.
#
# An array a is a subset of an array b if a can be obtained from b by deleting
# some (possibly zero) elements of b.
from functools import reduce
from typing import List
def powerset(arr):
    size = len(arr)
    for i in range(1 << size):
        yield [arr[j] for j in range(size) if i & (1 << j)]

class Solution:
    @staticmethod
    def powerset(arr):
        size = len(arr)
        for i in range(1 << size):
            yield [arr[j] for j in range(size) if i & (1 << j)]

    def subsetXORSum(self, nums: List[int]) -> int:
        count = 0
        for seq in powerset(nums):
            count+=reduce(lambda x,y: x^y,seq,0)
        return count
