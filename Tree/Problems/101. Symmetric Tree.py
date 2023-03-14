# link   : https://leetcode.com/problems/symmetric-tree/
# author : Mohamed Ibrahim

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(root1,root2):
            if (not root1 and not root2):
                return True
            if root1 is None or root2 is None:
                return False

            if root1.val == root2.val:
                return dfs(root1.left,root2.right) and dfs(root1.right,root2.left)

        return dfs(root.left,root.right)
        
        
