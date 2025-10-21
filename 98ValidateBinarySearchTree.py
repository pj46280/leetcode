# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(LOW, node, HIGH):
            if not node:
                return True
            if not (LOW < node.val < HIGH):
                return False
            return dfs(LOW, node.left, node.val) and dfs(node.val, node.right, HIGH)

        return dfs(float('-inf'), root, float('inf'))


