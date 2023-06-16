from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if self.can_merge(left, right, interval[0], interval[1]):
                right = max(right, interval[1])
            else:
                res.append((left, right))
                left = interval[0]
                right = interval[1]
        res.append((left, right))
        return res

    def can_merge(self, a_left, a_right, b_left, b_right):
        if a_left > b_left:
            return self.can_merge(b_left, b_right, a_left, a_right)
        if a_right >= b_left and a_left <= b_right:
            return True
        return False


if __name__ == "__main__":
    print(
        Solution().merge(
            [
                [0, 0], [1, 2], [5, 5],
                [2, 4], [3, 3], [5, 6],
                [5, 6], [4, 6], [0, 0],
                [1, 2], [0, 2], [4, 5],
            ]
        )
    )
