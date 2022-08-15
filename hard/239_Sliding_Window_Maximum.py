# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position.
#
# Return the max sliding window.

# TAG: Sliding window, Queue, Heap(Priority queue), Monotonic queue
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):

        deq = deque()
        for i in range(k):
            while len(deq) > 0 and deq[0][0] < nums[i]:
                deq.popleft()
            deq.appendleft([nums[i], i])

        window_start = 1
        res = []
        for window_end in range(k, len(nums)):
            res.append(deq[-1][0])
            while len(deq) > 0 and deq[0][0] < nums[window_end]:
                deq.popleft()
            while len(deq) > 0 and deq[-1][1] < window_start:
                deq.pop()
            deq.appendleft([nums[window_end], window_end])
            window_start += 1
        res.append(deq[-1][0])
        return res
