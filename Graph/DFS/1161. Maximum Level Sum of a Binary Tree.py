# link   : https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree
# author : Mohamed Ibrahim 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(int)
        def dfs(node,level):
            if not node:
                return
            d[level] += node.val
            dfs(node.left , level+1)
            dfs(node.right , level+1)

        dfs(root,0)
        mn = max(d.values())
        for val in d:
            if d[val] == mn:return val+1
