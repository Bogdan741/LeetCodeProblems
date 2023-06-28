from typing import List
from collections import defaultdict
import heapq


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int,
    ) -> float:
        weighted_graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            weighted_graph[u].append((v, succProb[i]))
            weighted_graph[v].append((u, succProb[i]))

        max_prob = [0.0] * n
        max_prob[start] = 1.0

        pq = [(-1.0, start)]
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)
            if cur_node == end:
                return -cur_prob

            for adj_node, prob in weighted_graph[cur_node]:
                if -cur_prob * prob > max_prob[adj_node]:
                    max_prob[adj_node] = -cur_prob * prob
                    heapq.heappush(pq, (-max_prob[adj_node], adj_node))
        return 0.0
