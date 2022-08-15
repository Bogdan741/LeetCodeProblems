# You are given an integer array arr. You can choose a set of integers and
# remove all the occurrences of these integers in the array.
#
# Return the minimum size of the set so that at least half of the integers of
# the array are removed.

from typing import List
from collections import Counter
from queue import PriorityQueue


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        total = sum(count.values())
        priority = PriorityQueue()
        for val in count.values():
            priority.put(-val)

        current = 0
        counter = 0
        while current * 2 < total:
            current += -priority.get()
            counter += 1

        return counter


class Solution1:
    def minSetSize(self, arr: List[int]) -> int:
        total_count = 0
        for index, count in enumerate(sorted(Counter(arr).values(), reverse=True)):
            total_count += count
            if total_count >= len(arr) // 2:
                return index + 1

        return 0


if __name__ == "__main__":
    print(Solution().minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
