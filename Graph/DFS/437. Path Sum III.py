# link   : https://leetcode.com/problems/path-sum-iii/description/
# author : Mohamed Ibrahim

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.cnt = 0
        def dfs(root , cur_Sum):
            if not root:return

            cur_Sum+=root.val
            if cur_Sum - targetSum in freq:
                self.cnt+= freq[cur_Sum - targetSum]
            freq[cur_Sum]+=1

            dfs(root.left , cur_Sum)
            dfs(root.right , cur_Sum)
            freq[cur_Sum] -=1




        freq = defaultdict(int)
        freq[0] = 1
        dfs(root,0)
        return self.cnt
      
