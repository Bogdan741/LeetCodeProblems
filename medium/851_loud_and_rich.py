## There is a group of n people labeled from 0 to n - 1 where each person has a
## different amount of money and a different level of quietness.
##
## You are given an array richer where richer[i] = [ai, bi] indicates that ai has
##     more money than bi and an integer array quiet where quiet[i] is the
##     quietness of the ith person. All the given data in richer are logically
## correct (i.e., the data will not lead you to a situation where x is richer than
##          y and y is richer than x at the same time).
##
## Return an integer array answer where answer[x] = y if y is the least quiet
## person (that is, the person y with the smallest value of quiet[y]) among all
## people who definitely have equal to or more money than the person x.

from typing import List
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for b, a in richer: # a < b
            graph[a].append(b)

        ans = [None for _ in range(n)]
        def dfs(node) -> int:
            if ans[node] is None:
                ans[node] = node
                for child in graph[node]:
                    cand = dfs(child)
                    if quiet[cand] < quiet[ans[node]]:
                        ans[node] = cand
            return ans[node]
        return list(map(dfs, list(range(n-1,-1,-1))))[::-1]
