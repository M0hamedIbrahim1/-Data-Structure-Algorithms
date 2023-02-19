# link   : https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
# author : Mohamed Ibrahim


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root] if root else [])
        res = []
        while queue:
            level = []
            length = len(queue)
            for i in range(length):
                root = queue.popleft()
                level.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            level = reversed(level) if len(res) % 2 else level
            res.append(level)
        return res
      
      
      
