# Given the root of a binary tree and an integer targetSum, return true if the
# tree has a root-to-leaf path such that adding up all the values along the
# path equals targetSum.
#
# A leaf is a node with no children.

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    __slots__ = []

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )
