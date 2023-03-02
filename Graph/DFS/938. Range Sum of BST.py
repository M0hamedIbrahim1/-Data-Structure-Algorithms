# link   : https://leetcode.com/problems/range-sum-of-bst/
# author : Mohamed Ibrahim



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        Sum = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val >= low and node.val <= high:
                Sum+=node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return Sum
        
        
