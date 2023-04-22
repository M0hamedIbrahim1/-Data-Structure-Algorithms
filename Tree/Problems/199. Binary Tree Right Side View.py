# link   : https://leetcode.com/problems/binary-tree-right-side-view/description/
# author : Mohamed Ibrahim

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        visited = set()
        def dfs(root,level):
            if not root:
                return
            if level not in visited:    
                ans.append(root.val)
            visited.add(level)
            
            dfs(root.right,level+1)     
            dfs(root.left,level+1)

        dfs(root,0)      
        return ans
        
