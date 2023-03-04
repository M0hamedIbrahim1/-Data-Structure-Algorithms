# link    : https://leetcode.com/problems/same-tree/description
# author  : Mohamed Ibrahim


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            if not p and not q: return True
            if not p or not q or p.val != q.val: return False

            return dfs(p.left,q.left) and dfs(p.right,q.right)
        return dfs(p,q)


