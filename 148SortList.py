# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l, r):
            dummy = ListNode(0)
            tail = dummy
            while l and r:
                if l.val < r.val:
                    tail.next = l
                    l = l.next
                else:
                    tail.next = r
                    r = r.next
                tail = tail.next
            
            while l:
                tail.next = l
                l = l.next
                tail = tail.next

            while r:
                tail.next = r
                r = r.next
                tail = tail.next

            return dummy.next

        def merge_sort(head):
            if not head or not head.next:
                return head
            slow, fast = head, head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            left = head
            right = slow.next
            slow.next = None

            left = merge_sort(left)
            right = merge_sort(right)
            return merge(left, right)

        return merge_sort(head)

