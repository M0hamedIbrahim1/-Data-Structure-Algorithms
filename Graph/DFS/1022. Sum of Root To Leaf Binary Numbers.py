# link   : https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/
# author : Mohamed Ibrahim


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root,path,res):
            if not root:
                return None
            path+=str(root.val)
            dfs(root.left,path,res)
            dfs(root.right,path,res)
            if not root.left and not root.right:
                res.append(int(path,2))
        res = []
        dfs(root,'',res)
        return sum(res)
            
            
