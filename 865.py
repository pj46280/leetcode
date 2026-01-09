# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return 0, None

            left = dfs(node.left)
            right = dfs(node.right)

            if left[0] == right[0]:
                return left[0]+1, node
            elif left[0] > right[0]:
                return left[0] + 1, left[1]
            else:
                return right[0] + 1, right[1]


        return dfs(root)[1]


