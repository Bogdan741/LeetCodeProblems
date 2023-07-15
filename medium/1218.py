from typing import List, Dict
from collections import defaultdict
from bisect import bisect_right


# Too slow, but optimal if we need no a couter but a list
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        lookupDict: Dict[int, List[int]] = defaultdict(list)
        for idx, value in enumerate(arr):
            lookupDict[value].append(idx)

        n = len(arr)

        visited = [False] * n
        res = 0
        for i in range(n):
            if not visited[i]:
                j = i
                visited[j] = True
                counter = 1
                while j < n:
                    nextVal = arr[j] + difference
                    if nextVal in lookupDict:
                        indexes = lookupDict[nextVal]
                        # Find index of the nextVal greater than j
                        nextIdx = bisect_right(indexes, j)
                        # Check if it exists
                        if nextIdx < len(indexes):
                            j = indexes[nextIdx]
                            visited[j] = True
                        else:
                            break
                    else:
                        break
                    counter += 1

                res = max(res, counter)
        return res


class Solution1:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        answer = 1
        for a in arr:
            before_a = dp.get(a - difference, 0)
            dp[a] = before_a + 1
            answer = max(answer, dp[a])

        return answer
