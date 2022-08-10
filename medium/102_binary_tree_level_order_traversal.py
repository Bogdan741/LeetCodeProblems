from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.holder: dict = {}
        self.helpFunction(root, 0)
        res = []
        for payload in self.holder.values():
            res.append(payload)
        return res

    def helpFunction(self, node: Optional[TreeNode], level: int) -> None:
        if(len(self.holder.items()) < level + 1):
            self.holder[level] = []
        if(node):
            self.holder[level].append(node.val)
            if(node.left):
                self.helpFunction(node.left, level+1)
            if(node.right):
                self.helpFunction(node.right, level+1)
        return None
