# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To
# work on the ith job, you have to finish all the jobs j where 0 <= j <
# i).
#
# You have to finish at least one task every day. The difficulty of a job
# schedule is the sum of difficulties of each day of the d days. The difficulty
# of a day is the maximum difficulty of a job done on that day.
#
# You are given an integer array jobDifficulty and an integer d. The difficulty
# of the ith job is jobDifficulty[i].
#
# Return the minimum difficulty of a job schedule. If you cannot find a
# schedule for the jobs return -1.


from typing import List
import math
import functools

# Naive solution (TLE without memoization)
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @functools.lru_cache(None)
        def helpFunciton(index, d) -> int:
            if d == 1:
                return max(jobDifficulty[index:])

            res = math.inf
            maxelement_before_i = jobDifficulty[index]
            for i in range(index + 1, len(jobDifficulty) - d + 2):
                res = min(res, helpFunciton(i, d - 1) + maxelement_before_i)
                maxelement_before_i = max(maxelement_before_i, jobDifficulty[i])
            return res

        res = helpFunciton(0, d)
        return -1 if res == math.inf else res


if __name__ == "__main__":
    print(Solution().minDifficulty([7, 1, 7, 1, 7, 1], 3))
