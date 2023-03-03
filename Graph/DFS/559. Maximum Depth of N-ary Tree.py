# link   : https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
# author : Mohamed Ibrahim

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:return 0
        self.mx = 1
        def dfs(root,d):
            
            if not root: return
            self.mx = max(self.mx,d)
            for i in root.children:
                dfs(i,d+1)
        dfs(root,1)
        return self.mx
        
        
