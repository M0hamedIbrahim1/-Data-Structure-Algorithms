# link   : https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
# author : Mohamed Ibrahim

# In-order 
class Solution(object):
    pre = -float('inf')
    res = float('inf')

    def minDiffInBST(self, root):
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res
        
        
