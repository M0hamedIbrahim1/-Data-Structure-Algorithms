# link   : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
# author : Mohamed Ibrahim


            
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)

        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root

        return l or r
