from collections import Counter
from functools import cmp_to_key
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        def cmp(x, y):
            if x[1] == y[1]:
                if x[0] < y[0]:
                    return -1
                elif x[0] > y[0]:
                    return 1
                return 0
            return y[1] - x[1]

        count = Counter(words)

        res = map(
            lambda x: x[0],
            sorted(list(count.items()), key=cmp_to_key(cmp)),
        )
        return list(res)[:k]
