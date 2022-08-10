# You are given two identical eggs and you have access to a building with n
# floors labeled from 1 to n.
#
# You know that there exists a floor f where 0 <= f <= n such that any egg
# dropped at a floor higher than f will break, and any egg dropped at or below
# floor f will not break.
#
# In each move, you may take an unbroken egg and drop it from any floor x
# (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if
# the egg does not break, you may reuse it in future moves.
#
# Return the minimum number of moves that you need to determine with certainty
# what the value of f is.

import math
class Solution:
    # Stupid solution: x**2 + x >= 2 * n <=> (x(x+1)/2 = n) x is integral
    def twoEggDrop(self, n: int) -> int:
        return math.ceil((-1 + math.sqrt(1 + 8 * n))/2)
