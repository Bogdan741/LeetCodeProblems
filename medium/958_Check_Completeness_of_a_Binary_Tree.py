from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def traverse(node):
            if not node:
                return ""
            if node.left is None and node.right is None:
                return str(node.val)

            representation = (
                "(" + traverse(node.left) + ")" + str(node.val) + "(" + traverse(node.right) + ")"
            )
            return representation

        res = traverse(root)
        print(res)
        for i in range(res.find("()") + 1, len(res)):
            if res[i] != ')':
                return False
        return True
