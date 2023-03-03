# link   : https://leetcode.com/problems/evaluate-boolean-binary-tree/description/
# author : Mohamed Ibrahim


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root.val == 2:
                return dfs(root.left) or dfs(root.right)
            elif root.val == 3:
                return dfs(root.left) and dfs(root.right)
            if root.val == 1:
                return 1
            elif root.val == 0:
                return 0
            else:
                return None
        return dfs(root)
        
        
