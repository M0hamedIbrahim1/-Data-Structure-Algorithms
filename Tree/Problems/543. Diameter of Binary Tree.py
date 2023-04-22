# link   : https://leetcode.com/problems/diameter-of-binary-tree/description/
# author : Mohamed Ibrahim

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.mx_length = 0
        ans=[0]
        def dfs(tree):
            if not tree : return 0
            if not tree.left and not tree.right:
                return 1
            
            left = dfs(tree.left) 
            right = dfs(tree.right)
            self.mx_length = max(self.mx_length ,  (left+right))
            return 1+max(left , right)
        dfs(root)
        return self.mx_length
        
