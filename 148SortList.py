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



## Constant Space Solution

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

            return dummy.next, tail

        def split(head, step):
            for _ in range(step - 1):
                if not head:
                    break
                head = head.next

            if not head:
                return None

            second = head.next
            head.next = None
            return second

        def merge_sort(head):
            if not head or not head.next:
                return head
            
            length = 0
            node = head
            while node:
                length += 1
                node = node.next

            dummy = ListNode(0)
            dummy.next = head

            step = 1

            while step < length:
                pre, cur = dummy, dummy.next
                while cur:
                    left = cur
                    right = split(left, step)
                    cur = split(right, step)

                    merged_head, merged_tail = merge(left, right)
                    pre.next = merged_head
                    pre = merged_tail

                step *= 2
            
            return dummy.next

        return merge_sort(head)

