# link   : https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# author : Mohamed Ibrahim


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if root:
            queue.append(root)
        h = 0 
        while queue:
            h+=1
            q = len(queue)
            for i in range(q):
                node = queue.popleft()
                if not node.left and not node.right:
                    return h
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return h    
        
        
