# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        # 1 5 5 6
        # 1 != 5, node=5 -> else
        # 5 == 5, nxt=5, node=6
        while node:
            while node.next and node.val == node.next.val:
            # if node.next and node.val == node.next.val:
                # nxt = node.next
                node.next = node.next.next
            node = node.next

        return head
