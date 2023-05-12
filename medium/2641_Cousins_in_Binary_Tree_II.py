from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dp = {}

        # Fix
        def dfs(parent, child, depth):
            if child is None:
                return
            if depth in dp:
                if parent is not None:
                    dp[depth] += parent.val
            else:
                if parent is not None:
                    dp[depth] = child.val
                else:
                    dp[depth] = 0
            dfs(child, child.left, depth + 1)
            dfs(child, child.right, depth + 1)

        dfs(None, root, 0)

        def update(parent, child, depth):
            if child is None:
                return
            if parent is not None:
                sum = dp[depth] - parent.val
                child.val = sum
            else:
                child.val = 0
            update(child, child.left, depth + 1)
            update(child, child.right, depth + 1)

        update(None, root, 0)
        return root
