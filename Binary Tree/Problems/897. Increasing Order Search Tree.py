# link   : https://leetcode.com/problems/increasing-order-search-tree/
# author : Mohamed ibrahim

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []
        def dfs(root):
            if root.left:
                dfs(root.left)
            res.append(root.val)
            if root.right:
                dfs(root.right)
        dfs(root)
        roott = TreeNode(res[0])
        newtree = roott 
        for i in range(1,len(res)):
            newtree.right = TreeNode(res[i])
            newtree = newtree.right
        return roott
      
