# link   : https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
# author : Mohamed Ibrahim



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def sumNumbers(self, root: TreeNode | None) -> int:
    def dfs(node: TreeNode | None, path=0) -> None:
      if not node: return 0
      path = path * 10 + node.val
      if not node.left and not node.right:
        return path
      return dfs(node.left, path) + dfs(node.right, path)

    return dfs(root)
    
    
