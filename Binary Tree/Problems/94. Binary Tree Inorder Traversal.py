# link : https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# author : Mohamed Ibrahim

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def tree(root):
            if not root:
                return
            tree(root.left)
            res.append(root.val)
            tree(root.right)
        res = []
        tree(root)
        return res
        
        
