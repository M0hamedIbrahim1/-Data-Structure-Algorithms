# link   : https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
# author : Mohamed Ibrahim


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        res = []
        while queue:
            len_q = len(queue)
            Sum = 0
            for i in range(len_q):
                node = queue.popleft()
                Sum+=node.val
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
            res.append(Sum/len_q)
        return res
      
      
