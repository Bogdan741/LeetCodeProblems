class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        next = node.next
        node.next = next.next
        node.val = next.val
