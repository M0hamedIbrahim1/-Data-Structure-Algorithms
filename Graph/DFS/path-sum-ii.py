# Link : https://leetcode.com/problems/path-sum-ii/description/
# author : Mohamed Ibrahim

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(root,path,targetSum):

            if not root :
                return 
            if not root.left and not root.right:
                if targetSum-root.val == 0:
                    res.append(path+[root.val])
                return
            targetSum-= root.val
            dfs(root.left,path+[root.val],targetSum )
            dfs(root.right,path+[root.val],targetSum )



        dfs(root,[],targetSum )
        return res
        
