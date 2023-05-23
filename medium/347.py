from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket: List[None | List[int]] = [None for _ in range(len(nums) + 1)]

        for p in count:
            f = count[p]
            if bucket[f] is None:
                bucket[f] = []
            bucket[f].append(p)

        res = []
        pos = len(bucket) - 1
        while pos > -1 and len(res) < k:
            if bucket[pos] is not None:
                res.extend(bucket[pos])
            pos -= 1
        return res[:k]
