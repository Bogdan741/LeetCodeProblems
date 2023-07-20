from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        temp = None
        while head:
            # Keep the next node
            temp = head.next
            # Reverse the link
            head.next = prev
            # Update the previous node and the current node.
            prev = head
            head = temp
        return prev

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        r1 = self.reverseList(l1)
        r2 = self.reverseList(l2)

        total_sum = 0
        carry = 0
        ans = ListNode()
        while r1 or r2:
            if r1:
                total_sum += r1.val
                r1 = r1.next
            if r2:
                total_sum += r2.val
                r2 = r2.next

            ans.val = total_sum % 10
            carry = total_sum // 10
            head = ListNode(carry)
            head.next = ans
            ans = head
            total_sum = carry

        return ans.next if carry == 0 else ans


# The other solution without modifying input
# The idea is simple, first we do go from head to bottom adding them and keeping a carry when thay are the same power
# Then we reverse the resulting list removing the carry
class Solution1:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        n1 = self.size(l1)
        n2 = self.size(l2)
        l1C = l1
        l2C = l2

        res: Optional[ListNode] = ListNode(-1)
        cur = res

        while n1 > n2:
            node = ListNode(l1C.val)
            cur.next = node
            cur = node
            l1C = l1C.next
            n1 -= 1

        while n2 > n1:
            node = ListNode(l2C.val)
            cur.next = node
            cur = node
            l2C = l2C.next
            n2 -= 1

        while n1 > 0 and n2 > 0:
            node = ListNode(l2C.val + l1C.val)
            cur.next = node
            cur = node
            l2C = l2C.next
            l1C = l1C.next
            n2 -= 1
            n1 -= 1

        res = self.reverseList(res)

        cur = res
        carry = 0
        while cur and cur.next:
            cur.val, carry = (cur.val + carry) % 10, (cur.val + carry) // 10
            cur = cur.next

        if carry:
            cur.val = carry
            return self.reverseList(res)
        return self.reverseList(res).next

    def size(self, head: Optional[ListNode]):
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        return n

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        temp = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
