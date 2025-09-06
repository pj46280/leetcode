# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        prev = dummy

        while prev.next and prev.next.next:
            cur = prev.next
            adj = cur.next

            cur.next = adj.next
            adj.next = cur
            prev.next = adj

            prev = cur

        return dummy.next
