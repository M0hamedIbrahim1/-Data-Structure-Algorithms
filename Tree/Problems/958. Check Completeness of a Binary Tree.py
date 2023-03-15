# link   : https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/
# author : Mohamed Ibrahim


class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q = collections.deque([(root, 1)])
        res = []
        while q:
            u, coord = q.popleft()
            res.append(coord)
            if u.left:
                q.append((u.left, 2*coord))
            if u.right:
                q.append((u.right, 2*coord+1))
        return len(res) == res[-1]
        
