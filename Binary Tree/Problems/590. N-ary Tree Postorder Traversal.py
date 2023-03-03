# link   : https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# author : Mohamed Ibrahim


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(root):
            if not root:
                return
            for i in root.children:
                dfs(i)
            res.append(root.val)
        res = []
        dfs(root)
        return res

