from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        countDict = Counter(tasks)
        res = 0
        for count in countDict.values():
            if count <= 1:
                return -1
            else:
                res += count // 3
                if count % 3 != 0:
                    res += 1
        return res
