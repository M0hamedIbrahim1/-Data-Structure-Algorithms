# link   : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
# author : Mohamed Ibrahim

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bst(l,r):
            if l > r:
                return None

            mid = (l+r)//2
            root = TreeNode(nums[mid])
            root.left = bst(l,mid-1)
            root.right = bst(mid+1,r)
            return root
        return bst(0,len(nums)-1)
        
        
        
