# link : https://leetcode.com/contest/biweekly-contest-102/problems/cousins-in-binary-tree-ii/
# author : Mohamed Ibrahim

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels_sum = defaultdict(int)
        
        def dfs(node , level):
            if not node:
                return
            levels_sum[level]+= node.val
            dfs(node.left , level+1)
            dfs(node.right , level+1)
        
        def DFS(node , level):
            if not node:return
            
            if node.left and node.right:
                node.left.val = node.right.val = (levels_sum[level] - (node.left.val + node.right.val))
            elif node.left:
                node.left.val = levels_sum[level] - node.left.val
            elif node.right:
                node.right.val = levels_sum[level] - node.right.val
                
            DFS(node.left , level+1)
            DFS(node.right , level+1)
        
        dfs(root , 0)
        root.val = 0
        DFS(root,1)
        return root
