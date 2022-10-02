# Given the root of a binary tree, construct a string consisting of parenthesis
# and integers from a binary tree with the preorder traversal way, and return
# it.
#
# Omit all the empty parenthesis pairs that do not affect the one-to-one
# mapping relationship between the string and the original binary tree.


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        self.res: List[str] = []
        self.res.append(str(root.val))
        if root.left is None and root.right is not None:
            self.res.append("()")
        self.traverse(root.left)
        self.traverse(root.right)
        return ''.join(self.res)

    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.res.append("(")
        self.res.append(str(root.val))
        if root.left is None and root.right is not None:
            self.res.append("()")
        self.traverse(root.left)
        self.traverse(root.right)
        self.res.append(")")
