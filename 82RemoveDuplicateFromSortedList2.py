# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre, cur = dummy, head

        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next

        return dummy.next




[1, 2, 3, 3, 3, 4, 4, 5]

pre, cur, nex = None, 1, 2
pre, cur, nex = 1, 2, 3
pre, cur, nex = 2, 3, 3
pre, cur, nex = 2, 3, 3
pre, cur, nex = 2, 4, 4
pre, cur, nex = 2, 5, None

