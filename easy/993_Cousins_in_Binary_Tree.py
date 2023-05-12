from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        t = []

        def dfs(root, child, depth):
            if child is None:
                return None

            if child.val == y or child.val == x:
                t.append((root, depth + 1))

            dfs(child, child.left, depth + 1)
            dfs(child, child.right, depth + 1)

        dfs(None, root, 0)
        f = t[0]
        s = t[1]
        return f[0] != s[0] and f[1] == s[1]
