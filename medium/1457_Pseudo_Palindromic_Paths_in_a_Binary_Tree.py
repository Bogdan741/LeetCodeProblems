class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional
from functools import reduce


# TODO: Not finished
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.parity = {i: 0 for i in range(10)}
        return self.traverse(root)

    def traverse(self, root) -> int:
        res = 0
        if root is None:
            return res
        self.parity[root.val] += 1
        if root.left is None and root.right is None:
            count = sum(self.parity.values())
            if count > 0 and count % 2 == 0:
                return (
                    1
                    if reduce(
                        lambda y, x: y and (x % 2 == 0), self.parity.values(), True
                    )
                    else 0
                )
            else:
                oneCountNotFound = True
                flag = True
                for i in self.parity.values():
                    if i % 2 == 0 or oneCountNotFound:
                        if i % 2 == 1:
                            oneCountNotFound = False
                    else:
                        flag = False
                        break
                return flag

