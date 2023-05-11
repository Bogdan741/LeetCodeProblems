from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:

        cnt = collections.defaultdict(int)
        res = []

        def traverse(node):
            if not node:
                return ""
            representation = (
                "(" + traverse(node.left) + ")" + str(node.val) + "(" + traverse(node.right) + ")"
            )
            cnt[representation] += 1
            if cnt[representation] == 2:
                res.append(node)
            return representation

        traverse(root)
        return res
