from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        res = []
        level = 0

        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    temp.append(node.val)
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
            
            if level%2:
                temp.reverse()

            res.append(temp)
            level += 1

        return res

