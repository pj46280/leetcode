# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        mx = -inf
        res = 0
        level = 1

        while q:
            total = 0
            for _ in range(len(q)):
                n = q.popleft()
                total += n.val
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)

            if total > mx:
                mx = total
                res = level
            
            level += 1

        return res
