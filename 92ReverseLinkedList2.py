# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        pre = dummy
        cur = dummy.next

        count = 1
        while count < left:
            pre = cur
            cur = cur.next
            count += 1

        before_left = pre
        left_node = cur
        prev = None
        for i in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        before_left.next = prev
        left_node.next = cur

        return dummy.next

