from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.helper(p, q)

    def helper(self, p, q) -> bool:
        if p is not None and q is not None:
            if p.val == q.val:
                return self.helper(p.left, q.left) and self.helper(p.right, q.right)
            return False
        return p == q
