from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        tmp = self.inorderTraversal(root.left)
        tmp.append(root.val)
        tmp.extend(self.inorderTraversal(root.right))
        return tmp
