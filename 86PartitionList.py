# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_list = ListNode()
        after_list = ListNode()

        before, after = before_list, after_list

        cur = head
        while cur:
            if cur.val < x:
                before.next = cur
                before = before.next
            else:
                after.next = cur
                after = after.next

            cur = cur.next

        after.next = None
        before.next = after_list.next

        return before_list.next


