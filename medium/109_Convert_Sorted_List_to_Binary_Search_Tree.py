class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        return self.toBST(head, None)

    def toBST(self, head, tail):
        if head == tail:
            return None
        slow = head
        fast = head
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next
        node = TreeNode(slow.val)
        node.left = self.toBST(head, slow)
        node.right = self.toBST(slow.next, tail)
        return node
