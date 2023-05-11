# link : https://leetcode.com/problems/maximum-width-of-binary-tree/description/
# author : Mohamed ibrahim

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([[root , 1 , 0]])
        res = 0
        prevLevel , prevNum = 0 , 1 
        while q:
            root , num , level = q.popleft()
            if level > prevLevel:
                prevLevel = level
                prevNum = num
            res = max(res ,num - prevNum +1)
            if root.left:
                q.append([root.left , 2*num , level+1])
            if root.right:
                q.append([root.right , 2*num +1 , level+1])
        return res
        
