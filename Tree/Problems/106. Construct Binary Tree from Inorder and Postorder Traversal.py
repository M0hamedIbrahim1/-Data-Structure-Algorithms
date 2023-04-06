# link   : https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
# author : Mohamed Ibrahim

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        x = postorder.pop()
        root = TreeNode(x)
        indx = inorder.index(x)
        root.right = self.buildTree( inorder[indx+1:] , postorder)
        root.left = self.buildTree( inorder[:indx] , postorder)
        return root

        
        
