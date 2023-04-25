# link   : https://leetcode.com/problems/balanced-binary-tree/description/
# author : Mohamed Ibrahim


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left - right) >= 2:
                self.ans = False

            return 1+max(left , right)
        dfs(root)
        return self.ans 
        
