# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left) 
            right = dfs(node.right)  

            return node.val + left + right

        def solve(node):
            if not node: return 0
            left = solve(node.left) 
            right = solve(node.right) 
            nonlocal res
            res = max(res, left * (total - left), right * (total - right))

            return left + right + node.val

        res = 0
        total = dfs(root)
        solve(root)

        return res % (10**9 + 7)
        

