import heapq
from typing import List, Optional


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pr = []
        for i, el in enumerate(tasks):
            pr.append([el[1], i, el[0]])
        tasks = sorted(pr, key=lambda x: (x[2], x[0]))
        heap = []
        res = []
        time = 1
        while len(tasks) > 0 or len(heap) > 0:
            while len(tasks) > 0 and tasks[0][2] <= time:
                first = tasks.pop(0)
                heapq.heappush(heap, first)
            if len(heap) == 0:
                first = tasks.pop(0)
                time += first[2] - 1
                heapq.heappush(heap, first)

            item = heapq.heappop(heap)
            res.append(item[1])
            time += item[0]
        return res
