import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        queue = []
        if 2 * candidates >= n:
            for i, cost in enumerate(costs, 0):
                # Here 1 means nothing
                # cause we do not need to push any element to the queue any more
                heapq.heappush(queue, (cost, i, 1))
            costs = []
        else:
            for i in range(0, candidates):
                heapq.heappush(queue, (costs[i], i, 1))
                heapq.heappush(queue, (costs[n - i - 1], n - i - 1, -1))

            costs = costs[candidates : n - candidates]

        l = candidates
        r = n - candidates - 1

        total_cost = 0
        count = k
        while len(queue) > 0 and count > 0:
            (cost, _, pos) = heapq.heappop(queue)
            total_cost += cost
            if len(costs) > 0:
                if pos == 1:
                    l += 1
                    heapq.heappush(queue, (costs.pop(0), l, pos))
                elif pos == -1:
                    r -= 1
                    heapq.heappush(queue, (costs.pop(), r, pos))
            count -= 1

        return total_cost


# Same idea but different implementation (but it's faster)
class Solution1:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # head_workers stores the first k workers.
        # tail_workers stores at most last k workers without any workers from the first k workers.
        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates, len(costs) - candidates) :]
        heapq.heapify(head_workers)
        heapq.heapify(tail_workers)

        answer = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates

        for _ in range(k):
            if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]:
                answer += heapq.heappop(head_workers)

                # Only refill the queue if there are workers outside the two queues.
                if next_head <= next_tail:
                    heapq.heappush(head_workers, costs[next_head])
                    next_head += 1
            else:
                answer += heapq.heappop(tail_workers)

                # Only refill the queue if there are workers outside the two queues.
                if next_head <= next_tail:
                    heapq.heappush(tail_workers, costs[next_tail])
                    next_tail -= 1

        return answer
