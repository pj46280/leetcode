# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def backtrack(start, end):
            if start > end:
                return [None]

            all_trees = []
            for i in range(start, end+1):
                left = backtrack(start, i-1)
                right = backtrack(i+1, end)

                for l in left:
                    for r in right:
                        root = TreeNode(i, l, r)
                        all_trees.append(root)

            return all_trees

        return backtrack(1, n)

