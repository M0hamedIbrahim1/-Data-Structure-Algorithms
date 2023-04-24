# link   : https://leetcode.com/problems/invert-binary-tree/description/
# author : Mohamed Ibrahim

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
        
        
